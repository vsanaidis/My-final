# Generated by Django 5.0.6 on 2024-07-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_notes_prerequisites'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='corerequisites',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]