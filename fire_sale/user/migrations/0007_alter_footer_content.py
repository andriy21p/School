# Generated by Django 4.0.4 on 2022-05-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_footer_footer_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='content',
            field=models.TextField(max_length=50000),
        ),
    ]
