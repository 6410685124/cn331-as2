# Generated by Django 4.2.5 on 2023-10-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0010_remove_class_semester_remove_class_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
