# Generated by Django 5.1.5 on 2025-01-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
                ('publicationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
