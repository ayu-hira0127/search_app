# forms.py
from django import forms
from .models import Product, ProductImage
from .widgets import MultipleFileInput

class SearchForm(forms.Form):
    query = forms.CharField(
        label='検索キーワード',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '検索したいキーワードを入力'})
    )

class ProductForm(forms.ModelForm):
    images = forms.FileField(widget=MultipleFileInput(), required=False, label='画像ファイル')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']

    def save(self, commit=True):
        instance = super().save(commit)
        return instance