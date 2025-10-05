from django import forms
from django.contrib.auth.hashers import make_password
from .models import TblUser

class CustomUserCreationForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'register-input',
            'placeholder': 'Enter your email'
        })
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'register-input',
            'placeholder': 'Choose a username'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'register-input',
            'placeholder': 'Create a password'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'register-input',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = TblUser
        fields = ['email', 'username']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if TblUser.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if TblUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user