# Generated by Django 4.0.4 on 2022-05-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='footer_page',
            field=models.SmallIntegerField(choices=[(1, 'Conduct'), (2, 'Privacy'), (3, 'Security'), (4, 'Cookies')]),
        ),
    ]