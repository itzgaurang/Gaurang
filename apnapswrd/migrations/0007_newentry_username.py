# Generated by Django 3.0.5 on 2020-05-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apnapswrd', '0006_newentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='newentry',
            name='username',
            field=models.CharField(default='username', max_length=280),
        ),
    ]