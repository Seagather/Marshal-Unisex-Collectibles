from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Full Contact form ommiting responded field """

    class Meta:
        model = Contact
        fields = [
            'Customer_Service',
            'Full_Name',
            'Phone_Number',
            'Email_Address',
            'Main_Message',
        ]
