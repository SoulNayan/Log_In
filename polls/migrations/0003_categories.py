# Generated by Django 5.1.2 on 2024-12-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Categories_image/')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
    ]
