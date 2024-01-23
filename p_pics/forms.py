from django import forms
from .models import UserImage

class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']
        # You can customize this form based on your requirements
