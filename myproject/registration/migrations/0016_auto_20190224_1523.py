# Generated by Django 2.1.5 on 2019-02-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20190220_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='category',
            field=models.CharField(blank=True, choices=[('1Jr', 'One Youth Division ($70)'), ('2Jr_Wt', '2 Youth Divisions - Up One Weight ($105)'), ('2Jr_Age', '2 Youth Divisions - Up One Age ($105)'), ('1Jr_1SrNon', '1 Youth + 1 Senior Non-Elite ($105)'), ('1Jr_1Sr', '1 Youth + 1 Senior Elite Division ($125)'), ('1Nv', '1 Non-Elite Senior Division ($70)'), ('2Nv', '2 Non-Elite Senior Divisions ($105)'), ('1Nv_1Vt', '1 Novice and 1 Veteran ($105)'), ('1Nv_1Sr', '1 Non-Elite + 1 Elite Senior Division (125)'), ('1Sr', '1 Senior Elite Division ($90)'), ('2Sr', '2 Senior Elite Divisions ($150)'), ('1Vt', '1 Veteran Division ($70)'), ('1Vt_1SrNon', '1 Veteran and 1 Senior Non-Elite Division ($125)'), ('1Vt_1Sr', '1 Veteran and 1 Senior Elite Division ($125)')], max_length=10, null=True, verbose_name='Divisions'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=22, null=True, verbose_name='Tel. #'),
        ),
    ]
