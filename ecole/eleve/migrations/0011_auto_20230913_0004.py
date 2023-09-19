# Generated by Django 3.2 on 2023-09-12 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eleve', '0010_auto_20230901_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='statut_eleveM',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elevecem',
            name='statut_eleveMCEM',
            field=models.CharField(default='non', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elevepre',
            name='statut_eleveMpre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='eleveprim',
            name='statut_eleveMPrim',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
