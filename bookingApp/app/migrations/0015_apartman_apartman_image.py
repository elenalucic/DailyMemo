# Generated by Django 4.1.6 on 2024-06-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_delete_apartmanimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartman',
            name='apartman_image',
            field=models.ImageField(blank=True, null=True, upload_to='apartman_img/'),
        ),
    ]
