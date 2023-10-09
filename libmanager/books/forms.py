from django import forms
from django.forms import Form

from .models import *


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Не выбрано'
        self.fields['genre'].empty_label = 'Не выбрано'
        self.fields['pub_house'].empty_label = 'Не выбрано'
        self.url = "addbook"
    class Meta:
        model = Book
        fields = ['title', 'author', 'year','genre', 'category', 'pub_house', 'isbn', 'total_amount']

class FindBookForm(forms.Form):
    title = forms.CharField(max_length=255)
    url = "findbook"

class FindAuthorForm(forms.Form):
    author = forms.CharField(max_length=255)
    url = "findauthor"


class UseridForm(forms.Form):
    uid = forms.IntegerField(label="Номер читательского билета")
class AddTestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['title', 'content']