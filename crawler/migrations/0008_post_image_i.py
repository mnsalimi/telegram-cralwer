# Generated by Django 4.1 on 2022-08-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0007_alter_post_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_i',
            field=models.ImageField(blank=True, null=True, upload_to='hero_headshots/'),
        ),
    ]
