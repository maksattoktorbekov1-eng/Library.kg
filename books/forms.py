from django import forms
from .models import Book, Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['rating', 'text']
        widgets = {
            'rating': forms.NumberInput(attrs={'min':1, 'max':5}),
            'text': forms.Textarea(attrs={'rows':5})
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not 1 <= rating <= 5:
            raise forms.ValidationError("Ставьте оценку только от 1 до 5")
        return rating

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text.strip()) < 200:
            raise forms.ValidationError("Текст отзыва должен быть минимум 200 символов")
        return text

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Название книги'}),
            'author': forms.TextInput(attrs={'placeholder':'Автор'}),
            'description': forms.Textarea(attrs={'rows':5, 'placeholder':'Описание книги'}),
        }