# Generated by Django 5.0.6 on 2024-07-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.TextField(),
        ),
    ]
