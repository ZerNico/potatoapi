# Generated by Django 3.0.1 on 2019-12-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_date', models.IntegerField()),
                ('build_type', models.CharField(max_length=32)),
                ('device', models.CharField(max_length=32)),
                ('dish', models.CharField(max_length=32)),
                ('downloads', models.IntegerField(default=0)),
                ('filename', models.CharField(max_length=128)),
                ('md5', models.CharField(max_length=64, unique=True)),
                ('notes', models.TextField(blank=True, max_length=256, null=True)),
                ('size', models.IntegerField()),
                ('url', models.CharField(max_length=256)),
                ('version', models.CharField(max_length=32)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
