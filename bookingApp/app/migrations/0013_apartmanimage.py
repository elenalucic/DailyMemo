# Generated by Django 4.1.6 on 2024-06-01 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_apartman_apartman_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmanImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='apartman_img/')),
                ('apartman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.apartman')),
            ],
        ),
    ]
