# Generated by Django 5.1.1 on 2024-09-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='Devos/')),
                ('bio', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cars',
            name='price',
        ),
        migrations.AlterField(
            model_name='cars',
            name='img',
            field=models.ImageField(upload_to='Devos/'),
        ),
    ]
