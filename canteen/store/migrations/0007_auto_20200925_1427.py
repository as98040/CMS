# Generated by Django 3.1 on 2020-09-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200921_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.AddField(
            model_name='order',
            name='verification_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
