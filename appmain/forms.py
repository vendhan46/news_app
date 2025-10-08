from django import forms
from .models import ReaderOpinion
from .models import User

class ReaderOpinionForm(forms.ModelForm):
    class Meta:
        model = ReaderOpinion
        fields = ['name', 'email', 'message']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["phone", "address", "interested_field", "image"]