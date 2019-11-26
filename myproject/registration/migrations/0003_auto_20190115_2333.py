# Generated by Django 2.1.2 on 2019-01-15 23:33

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20190115_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='person',
            name='card_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='judo_card',
            field=models.CharField(choices=[('USJUDO', 'USA Judo'), ('USJA', 'USJA'), ('USJF', 'USJF')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='judo_club',
            field=models.CharField(max_length=100, null=True, verbose_name='Judo Club'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='Tel. #'),
        ),
        migrations.AddField(
            model_name='person',
            name='rank',
            field=models.CharField(max_length=20, null=True, verbose_name='Rank'),
        ),
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Sex'),
        ),
        migrations.AddField(
            model_name='person',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='Zip'),
        ),
    ]
