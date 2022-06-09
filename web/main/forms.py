from .models import News
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "text"]
        widgets = {"title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }
