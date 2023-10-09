# Generated by Django 4.2.5 on 2023-09-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='is_givedaway',
            field=models.BooleanField(default=False),
        ),
    ]