from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'Customer_Service',
        'Phone_Number',
        'Email_Address',
        'Main_Message',
        'responded',
    )


admin.site.register(Contact, ContactAdmin)
