from django import forms
from .models import Thread, Post


class ThreadCreateForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Your new thread title'}
                                )
                            )
    content = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    'placeholder': 'Your thread content',
                                    'class': 'new-class-name two',
                                    'id': 'my-id-for-textarea',
                                    'rows': 20,
                                    'cols': 120
                                }
                            )
                        )


    class Meta:
        model = Thread
        fields = (
            'title',
            'content',
        )

class ThreadEditForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = (
            'title',
            'content',
        )

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(
        label='', required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your thread content',
                'class': 'form-control',
                'id': 'my-id-for-textarea',
                'rows': 5,
                'cols': 120
            }
        )
    )

    class Meta:
        model = Post
        fields = (
            'content',
        )
