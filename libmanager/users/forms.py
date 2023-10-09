from django import forms
from users.models import *

class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = "adduser"
        self.enctype = "multipart/form-data"
    class Meta:
        model = User
        fields = ["fio", "birthdate", "photo", "contacts"]

class FindUserForm(forms.Form):
    fio = forms.CharField(max_length=255)
    url = "finduser"