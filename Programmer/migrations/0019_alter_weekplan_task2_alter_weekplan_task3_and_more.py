# Generated by Django 4.1.7 on 2023-07-15 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Programmer', '0018_alter_refrence_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekplan',
            name='task2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weekplan_task2', to='Programmer.refrence'),
        ),
        migrations.AlterField(
            model_name='weekplan',
            name='task3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weekplan_task3', to='Programmer.refrence'),
        ),
        migrations.AlterField(
            model_name='weekplan',
            name='task4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weekplan_task4', to='Programmer.refrence'),
        ),
    ]
