# Generated by Django 3.1 on 2020-11-07 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('former_barcode', models.CharField(max_length=80)),
                ('favourite_barcode', models.CharField(max_length=80, unique=True)),
                ('email_user', models.EmailField(max_length=150)),
            ],
            options={
                'db_table': 'favourite',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('nutrition_grade', models.CharField(blank=True, max_length=1, null=True)),
                ('barcode', models.CharField(max_length=255)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('url_pic', models.CharField(blank=True, max_length=255, null=True)),
                ('store', models.CharField(blank=True, max_length=255, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('saturated_fat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sugar', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('salt', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('prd_cat', models.ForeignKey(db_column='prd_cat', on_delete=django.db.models.deletion.DO_NOTHING, to='food.category')),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
    ]
