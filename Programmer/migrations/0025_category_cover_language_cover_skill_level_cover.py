# Generated by Django 4.1.7 on 2023-07-22 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Programmer', '0024_refrence_category_refrence_keywords_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cover',
            field=models.ImageField(default='empty', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='language',
            name='cover',
            field=models.ImageField(default='empty', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='skill_level',
            name='cover',
            field=models.ImageField(default='empty', upload_to='images/'),
        ),
    ]
