# Generated by Django 4.2.6 on 2023-10-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_project_image_alter_skill_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/static/img/logos/'),
        ),
    ]
