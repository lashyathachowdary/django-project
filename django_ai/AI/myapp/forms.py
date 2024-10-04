from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name=forms.CharField(label='Your Name',max_length=100)
    email=forms.EmailField(label='Your Email')
    message=forms.CharField(widget=forms.Textarea,label='Message')
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']