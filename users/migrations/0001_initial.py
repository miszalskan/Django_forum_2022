# Generated by Django 4.1.5 on 2023-01-15 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('forget_password_token', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('forget_password_token', models.CharField(max_length=100)),
            ],
        ),
    ]
