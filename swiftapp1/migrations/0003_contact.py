# Generated by Django 5.1.3 on 2024-12-07 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiftapp1', '0002_remove_material_description_remove_material_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]