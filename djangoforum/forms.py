from django import forms
from django.contrib.auth.models import User
from simpleforum.models import UserProfile


class UserLoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password '}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password '}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password mismatched")
        return confirm_password


class UserEditForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)  # exclude user field from UserProfile model
