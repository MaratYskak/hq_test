# Generated by Django 4.2.5 on 2023-09-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hq_test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonview',
            name='last_viewed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
