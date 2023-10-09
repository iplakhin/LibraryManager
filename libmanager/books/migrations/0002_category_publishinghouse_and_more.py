# Generated by Django 4.2.5 on 2023-09-17 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='publishing_house',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.genres'),
        ),
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.genres'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='pub_house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.publishinghouse'),
        ),
        migrations.AddField(
            model_name='magazine',
            name='pub_house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.publishinghouse'),
        ),
    ]
