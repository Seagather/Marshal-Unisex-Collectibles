from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Full Contact form ommiting responded field """
    required_css_class = 'required'

    class Meta:
        model = Contact
        fields = [
            'Customer_Service',
            'Full_Name',
            'Phone_Number',
            'Email_Address',
            'Main_Message',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Full_Name'].widget.attrs.update({
            'class': 'text-muted',
            'placeholder': 'Full Name'})
        self.fields['Phone_Number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'tel'})
        self.fields['Email_Address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'E-mail'})
        self.fields['Main_Message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Message...'})
