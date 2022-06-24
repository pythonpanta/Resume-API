# Generated by Django 4.0.5 on 2022-06-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('skills', models.TextField()),
                ('photo', models.ImageField(default='no image', null=True, upload_to='userImage')),
                ('document', models.FileField(default='no image', null=True, upload_to='userDoc')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]