from django import forms
from django.forms.widgets import ClearableFileInput  # インポートを追加
from .models import Product, ProductImage

class SearchForm(forms.Form):
    query = forms.CharField(
        label='検索キーワード',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '検索したいキーワードを入力'})
    )

class CustomClearableFileInput(ClearableFileInput):
    allow_multiple_selected = True

class ProductForm(forms.ModelForm):
    images = forms.FileField(
        widget=CustomClearableFileInput(attrs={'multiple': True}),
        required=False,
        label='画像ファイル'
    )

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'images']
        labels = {
            'name': '商品名',
            'description': '商品説明',
            'price': '価格',
            'category': 'カテゴリ',
        }

    def clean_images(self):
        images = self.files.getlist('images')
        if len(images) > 10:
            raise forms.ValidationError('画像は最大10枚までアップロード可能です。')
        
        for image in images:
            if image.size > 5 * 1024 * 1024:  # 5MB以上の画像を弾く例
                raise forms.ValidationError('画像サイズは5MB以下である必要があります。')
        return images

    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit=commit)
        for uploaded_file in self.files.getlist('images'):
            ProductImage.objects.create(product=instance, image=uploaded_file)
        return instance