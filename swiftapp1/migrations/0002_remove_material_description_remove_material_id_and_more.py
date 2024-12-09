# Generated by Django 5.1.3 on 2024-12-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftapp1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='description',
        ),
        migrations.RemoveField(
            model_name='material',
            name='id',
        ),
        migrations.AlterField(
            model_name='material',
            name='image',
            field=models.ImageField(upload_to='material_images/'),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]