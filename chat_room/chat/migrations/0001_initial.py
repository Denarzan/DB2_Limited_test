# Generated by Django 3.2 on 2021-04-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(db_index=True, max_length=128, verbose_name='Author')),
                ('email', models.CharField(max_length=128, verbose_name='Email')),
                ('text', models.CharField(max_length=1028, verbose_name='Text')),
                ('create_date', models.DateTimeField(verbose_name='Create date')),
                ('update_date', models.DateTimeField(verbose_name='Update date')),
            ],
        ),
    ]
