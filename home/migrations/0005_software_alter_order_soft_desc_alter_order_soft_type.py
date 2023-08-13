# Generated by Django 4.1.2 on 2023-08-10 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_getjob_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('softwareName', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='soft_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='soft_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.software'),
        ),
    ]