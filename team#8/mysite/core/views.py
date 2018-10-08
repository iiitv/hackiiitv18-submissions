from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serialisers import profile_dataSerialiser
from .models import Profile, bmm
import json

from mysite.core.forms import SignUpForm
from mysite.core.tokens import account_activation_token


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            Profile.update_user_profile(user, 'biology', form.cleaned_data['email'])
            bmm.update_body_measurements(user, form.cleaned_data['height'], form.cleaned_data['weight'])
            current_site = get_current_site(request)
            subject = 'Activate Your MediCare Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            from_email = settings.EMAIL_HOST_USER

            user.email_user(subject, message, from_email)


            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


class getprofile(APIView):
    def get(self, request):
        users = Profile.objects.all()
        serializer2 = profile_dataSerialiser(users, many=True)
        return Response(serializer2.data)

class getbmm(APIView):
    def get(self, request):
        users = bmm.objects.all()
        serializer2 = profile_dataSerialiser(users, many=True)
        return Response(serializer2.data)





