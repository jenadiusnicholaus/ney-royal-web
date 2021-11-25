# Generated by Django 3.2.9 on 2021-11-25 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='profile_files')),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('location', models.CharField(max_length=20, null=True)),
                ('bio', models.TextField(blank=True, max_length=300, null=True)),
                ('region', models.CharField(blank=True, max_length=15, null=True)),
                ('district', models.CharField(blank=True, max_length=15, null=True)),
                ('ward', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
