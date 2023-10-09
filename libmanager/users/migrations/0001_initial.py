# Generated by Django 4.2.5 on 2023-09-13 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fio', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('photo', models.ImageField(height_field=300, upload_to='profiles/', width_field=200)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('contacts', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='BooksUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField()),
                ('is_expired', models.BooleanField(default=False)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='books.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.user')),
            ],
        ),
    ]
