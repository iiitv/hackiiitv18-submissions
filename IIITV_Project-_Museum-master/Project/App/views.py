from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View
from App.forms import LoginForm, RegisterForm

from App.forms import LoginForm, RegisterForm, ProjectForm
from App.models import Project


def index(request):
    #project=Project()
    projects=Project.objects.all()
    return render(request, 'index.html',{'projects':projects})

def project_detail(request, pk):
    print(pk)
    project = Project.objects.get(pk=pk)
    print(project)
    return render(request, './project_detail.html', {'project': project})

class ProjectFormView(View):
    form_class = ProjectForm
    template_name = 'form_project.html'

    # sends query and form on request
    def get(self, request):
        form = self.form_class(None)
        print(form)
        return render(request, self.template_name,
                      {'form': form})

    # authenticates user request
    def post(self, request):
        pass
        # form = self.form_class(request.POST)

        # if form.is_valid():

        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']

        #     user = authenticate(username=username, password=password)
        #     print(user)
        #     if user is not None:
        #         login(request, user)
        #         messages.success(request, "Logged in Successfully")
        #         return redirect('/')
        #     else:
        #         messages.error(request, "Incorrect Credentials")
        #         return redirect('App:login')
        # else:
        #     messages.error(request, "Incorrect credentials")
        #     return render(request, self.template_name, {'form': form})

class ProjectFormView(View):
    form_class = ProjectForm
    template_name = 'form_project.html'

    # sends query and form on request
    def get(self, request):
        form = self.form_class(None)
        print(form)
        return render(request, self.template_name,
                      {'form': form})

    # authenticates user request
    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('/')
        else:
            messages.error(request, "Incorrect credentials")
            return render(request, self.template_name, {'form': form})



class LoginFormView(View):
    """Uses the LoginForm created in forms.py and handles 'GET' 'POST' requests
        from form_register.html """
    form_class = LoginForm
    template_name = 'form_login.html'

    # sends query and form on request
    def get(self, request):
        form = self.form_class(None)
        print(form)
        return render(request, self.template_name,
                      {'form': form})

    # authenticates user request
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('/')
            else:
                messages.error(request, "Incorrect Credentials")
                return redirect('App:login')
        else:
            messages.error(request, "Incorrect credentials")
            return render(request, self.template_name, {'form': form})


class RegisterFormView(View):
    """Uses the RegisterForm created in forms.py and handles 'GET' 'POST' requests
        from form_register.html """
    form_class = RegisterForm
    template_name = 'form_register.html'

    # sends query and form on request
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,
                      {'form': form})

    # stores data to database on request and authenticates the user
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            user.set_password(password)
            if password == confirm_password:
                user.save()
                messages.success(request, "Registered Successfully")
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')
            else:
                messages.error(request, "Incorrect credentials")
                return render(request, self.template_name, {'form': form})
        else:
            messages.error(request, "Incorrect credentials")
            return render(request, self.template_name, {'form': form})


def signout(request):
    """logs out the user on request"""
    logout(request)
    return redirect('App:index')

def AboutUs(request):
    return render(request,'aboutus.html')
