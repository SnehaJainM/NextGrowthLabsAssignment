# Generated by Django 4.2.11 on 2024-09-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminApps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_image', models.ImageField(upload_to='app_images/')),
                ('app_name', models.CharField(max_length=200)),
                ('app_link', models.URLField()),
                ('app_category', models.CharField(choices=[('category1', 'Educational apps'), ('category2', 'Lifestyle apps'), ('category3', 'Social media apps'), ('category4', 'Productivity apps'), ('category5', 'Entertainment apps'), ('category6', 'Game apps')], max_length=20)),
                ('app_subcategory', models.CharField(choices=[('subcategory1', 'Subcategory 1'), ('subcategory2', 'Subcategory 2')], max_length=20)),
            ],
        ),
    ]
