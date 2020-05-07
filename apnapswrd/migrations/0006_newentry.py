# Generated by Django 3.0.5 on 2020-05-01 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apnapswrd', '0005_auto_20200430_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='newentry',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('entryname', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=280)),
                ('password', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
