# Generated by Django 4.0.4 on 2022-05-12 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_checkout_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='country',
            field=models.ForeignKey(blank=True, default=243, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.country'),
        ),
    ]