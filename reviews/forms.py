from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Full Review form """
    required_css_class = 'required'

    class Meta:
        model = Review
        required_css_class = 'required'
        fields = [
            'title',
            'body',
        ]
