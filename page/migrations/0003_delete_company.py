# Generated by Django 4.2 on 2023-05-08 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_rename_name_prantship_company_name_partners'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]
