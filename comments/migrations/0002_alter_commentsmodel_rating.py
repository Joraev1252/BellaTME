# Generated by Django 4.0.6 on 2022-07-16 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsmodel',
            name='rating',
            field=models.CharField(choices=[('⭐️', 1), ('⭐️⭐️', 2), ('⭐️⭐️⭐️', 3), ('⭐️⭐️⭐️⭐️', 4), ('⭐️⭐️⭐️⭐️⭐️', 5)], max_length=255),
        ),
    ]
