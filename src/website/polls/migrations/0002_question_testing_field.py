# Generated by Django 3.1.3 on 2020-11-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='testing_field',
            field=models.IntegerField(null=True),
        ),
    ]
