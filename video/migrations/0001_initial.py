# Generated by Django 4.0.6 on 2022-07-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_original', models.FileField(upload_to='')),
                ('video_240', models.FileField(blank=True, null=True, upload_to='')),
                ('video_360', models.FileField(blank=True, null=True, upload_to='')),
                ('convert_time', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]