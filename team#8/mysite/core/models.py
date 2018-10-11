from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.', default = 'abc@gxyz.com')
    timeSpent = models.IntegerField()
    email_confirmed = models.BooleanField(default=False)

    @staticmethod
    def update_user_profile(user, b, mail):
        instanc = Profile.objects.create(user=user, bio = b, email = mail, timeSpent = 0, email_confirmed = True)
        instanc.save()



class bmm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timeSpent = models.IntegerField(default = 0)
    height = models.DecimalField( help_text='Please enter your height',default=0.0, decimal_places = 4, max_digits = 10)
    weight = models.DecimalField( help_text='Please enter your weight', default=0.0, decimal_places = 4, max_digits = 10)
    BMI = models.DecimalField(decimal_places = 4, max_digits = 10)

    @staticmethod
    def update_body_measurements(user, h, w):
        B = h / (w * w)
        instance = bmm.objects.create(user=user, timeSpent = 0, height = h, weight = w,  BMI = B)
        instance.save()