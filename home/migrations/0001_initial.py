# Generated by Django 4.1.2 on 2023-03-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('password', models.TextField(max_length=8)),
                ('con_password', models.TextField(max_length=8)),
                ('fullname', models.TextField(max_length=20)),
                ('username', models.TextField(max_length=20)),
                ('education', models.TextField(max_length=300)),
                ('qualification', models.TextField(max_length=300)),
            ],
        ),
    ]
