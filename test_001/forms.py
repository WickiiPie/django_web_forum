from django import forms

from django.contrib.auth.models import User

from forum.models import user_profile

class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Enter Password '}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Confirm Password '}))
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
        model = user_profile
        exclude =  ('user',)   #exclude user field from user_profile model
