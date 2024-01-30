from django import forms
from.models import Book


class MemberForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','description','price']
