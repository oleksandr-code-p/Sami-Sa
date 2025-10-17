from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True,widget=forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'placeholder': 'Enter your email'}))
    username = forms.CharField(max_length = 10,widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
            'placeholder': 'Choose a username'
        }))
    password1 = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
            'placeholder': 'Enter password'
        }))
    password2 = forms.CharField(label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
            'placeholder': 'Enter password'
        }))

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length = 10,widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
            'placeholder': 'Choose a username'
        }))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
            'placeholder': 'Enter password'
        }))

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'
        }))
    first_name = forms.CharField(required = True,widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'
        }))
    last_name = forms.CharField(required = True,widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'
        }))
    class Meta():
        model = User
        fields = ('email','first_name','last_name')
class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500',
            'rows': 4,
            'placeholder': 'Tell us about yourself...'
        })
    )
    class Meta():
        model = UserProfile
        fields = ('bio',)
