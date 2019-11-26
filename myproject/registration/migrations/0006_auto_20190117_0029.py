# Generated by Django 2.1.2 on 2019-01-17 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20190116_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='senior_advanced',
            options={'verbose_name': 'Senior Elite'},
        ),
        migrations.AlterModelOptions(
            name='senior_novice',
            options={'verbose_name': 'Senior Novice'},
        ),
        migrations.AlterField(
            model_name='senior_advanced',
            name='actual_weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Weigh In Weight (kgs)'),
        ),
        migrations.AlterField(
            model_name='senior_advanced',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Weight (kgs)'),
        ),
        migrations.AlterField(
            model_name='senior_novice',
            name='actual_weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Weigh In Weight (kgs)'),
        ),
        migrations.AlterField(
            model_name='senior_novice',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Weight (kgs)'),
        ),
        migrations.AlterField(
            model_name='veteran',
            name='actual_weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Weigh In Weight (kgs)'),
        ),
        migrations.AlterField(
            model_name='veteran',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Weight (kgs)'),
        ),
    ]
