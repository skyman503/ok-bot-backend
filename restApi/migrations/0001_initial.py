# Generated by Django 3.2.4 on 2021-06-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('background', models.ImageField(upload_to='')),
            ],
        ),
    ]
