from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    height = forms.DecimalField( help_text='Please enter your height', decimal_places = 4, max_digits = 10)
    weight = forms.DecimalField( help_text='Please enter your weight', decimal_places = 4, max_digits = 10)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'height', 'weight')

    # def __init__(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields.['email'].widget = TextInput(attrs={
    #         'id': 'myCustomId',
    #         'class': 'myCustomClass',
    #         'name': 'myCustomName',
    #         'placeholder': 'myCustomPlaceholder'})
    
