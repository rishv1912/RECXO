# Generated by Django 4.1.2 on 2023-08-13 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_order_soft_type_remove_softwares_software_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='software',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.softwares'),
        ),
    ]
