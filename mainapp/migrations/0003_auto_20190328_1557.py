# Generated by Django 2.1.4 on 2019-03-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_video_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(default='default.mp4', upload_to='videos/'),
        ),
    ]