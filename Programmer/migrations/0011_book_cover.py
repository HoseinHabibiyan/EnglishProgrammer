# Generated by Django 4.1.7 on 2023-07-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Programmer', '0010_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='https://placehold.co/400x600?text=No+Cover', upload_to='images/'),
        ),
    ]
