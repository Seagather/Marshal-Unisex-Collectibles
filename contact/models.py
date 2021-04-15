from django.db import models


CUSTOMER_SERVICES = (
    ('general_enquiry', 'General Enquiry'),
    ('trade_your_watch', 'Trade Your Watch'),
    ('sell_your_watch', 'Sell Your Watch'),
    ('product_technical_assistance', 'Product Technical Assistance'),
    ('product_suggestion', 'Product Suggestion'),
    ('general_feedback', 'General Feedback'),
)


class Contact(models.Model):
    """ A model for contact submissions """

    class Meta:
        verbose_name_plural = 'Contact Page Submissions'

    Customer_Service = models.CharField(
        max_length=120,
        choices=CUSTOMER_SERVICES,
        default='general_enquiry',
        null=False,
        blank=False,

    )
    Full_Name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    Phone_Number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    Email_Address = models.CharField(
        max_length=90,
        null=False,
        blank=False,
    )
    Main_Message = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
    )
    responded = models.BooleanField(default=False)

    def __str__(self):

        return self.Full_Name
