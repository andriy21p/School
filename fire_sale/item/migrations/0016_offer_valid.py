# Generated by Django 4.0.4 on 2022-05-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_remove_item_item_item_hitcoun_e60e7c_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]
