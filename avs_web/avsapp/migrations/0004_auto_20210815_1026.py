# Generated by Django 3.2.5 on 2021-08-15 10:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('avsapp', '0003_alter_consultant_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='aggrement_plociy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='aggrement_service',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='consultant',
            name='aggrement_plociy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='consultant',
            name='aggrement_service',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='business_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='business_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
