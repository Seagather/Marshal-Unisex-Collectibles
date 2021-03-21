# Generated by Django 3.1.7 on 2021-03-21 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Service', models.CharField(choices=[('general_enquiry', 'General Enquiry'), ('trade_your_watch', 'Trade Your Watch'), ('sell_your_watch', 'Sell Your Watch'), ('product_technical_assistance', 'Product Technical Assistance'), ('product_suggestion', 'Product Suggestion'), ('general_feedback', 'General Feedback')], default='general_enquiry', max_length=120)),
                ('Full_Name', models.CharField(max_length=50)),
                ('Phone_Number', models.CharField(blank=True, max_length=20, null=True)),
                ('Email_Address', models.CharField(max_length=90)),
                ('Main_Message', models.TextField(max_length=3000)),
                ('responded', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Contact Page Submissions',
            },
        ),
    ]
