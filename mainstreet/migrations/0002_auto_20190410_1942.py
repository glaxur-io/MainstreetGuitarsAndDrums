# Generated by Django 2.2 on 2019-04-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstreet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='video',
        ),
        migrations.RemoveField(
            model_name='instruments',
            name='video',
        ),
        migrations.AddField(
            model_name='equipment',
            name='instagram',
            field=models.URLField(default='https://www.instagram.com/mainstreetvintageguitar/', max_length=300),
        ),
        migrations.AddField(
            model_name='instruments',
            name='instagram',
            field=models.URLField(default='https://www.instagram.com/mainstreetvintageguitar/', max_length=300),
        ),
    ]
