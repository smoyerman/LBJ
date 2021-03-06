# Generated by Django 2.1.5 on 2019-01-31 16:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_auto_20190124_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='person',
            name='card_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_of_Birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='person',
            name='judo_card',
            field=models.CharField(blank=True, choices=[('USJUDO', 'USA Judo'), ('USJA', 'USJA'), ('USJF', 'USJF')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='judo_club',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Judo Club'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Please use the following format: <em>+12223334444</em>.', max_length=128, null=True, verbose_name='Tel. #'),
        ),
        migrations.AlterField(
            model_name='person',
            name='rank',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Rank'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='person',
            name='us_citizen',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, null=True),
        ),
    ]
