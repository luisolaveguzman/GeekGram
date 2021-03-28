from django.forms import forms, ModelForm, URLInput, TextInput, Textarea, ClearableFileInput

from users.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'website', 'biography', 'phone_number', 'picture'
        ]
        widgets = {
            'website': URLInput(
                attrs={
                    'placeholder': 'Página web',
                    'class': 'form-control',
                    'max_length': 255,
                    'required': True
                }),
            'biography': Textarea(
                attrs={
                    'placeholder': 'Biografía',
                    'class': 'form-control',
                    'max_length': 1000,
                    'required': True
                }),
            'phone_number': TextInput(
                attrs={
                    'placeholder': 'Número telefónico',
                    'class': 'form-control',
                    'max_length': 255,
                    'required': True
                }),
            'picture': ClearableFileInput()
        }
