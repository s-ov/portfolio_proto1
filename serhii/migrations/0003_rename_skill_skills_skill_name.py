# Generated by Django 4.2.1 on 2023-05-30 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serhii', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='skill',
            new_name='skill_name',
        ),
    ]
