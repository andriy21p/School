# Generated by Django 4.0.4 on 2022-05-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('message', '0003_alter_message_msg_replied'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_sub_type', models.CharField(max_length=10000)),
                ('msg_sub_snippet', models.CharField(max_length=10000)),
            ],
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message_body',
            new_name='msg_body',
        ),
    ]