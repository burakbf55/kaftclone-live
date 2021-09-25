# Generated by Django 3.2.7 on 2021-09-23 08:07

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=200)),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlandi'), ('deleted', 'Silindi')], default='draft', max_length=10)),
                ('gender', models.CharField(choices=[('men', 'Erkek'), ('women', 'Kadin'), ('unisex', 'UnİSex')], default='unisex', max_length=6)),
                ('createt_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=200)),
                ('content', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='page')),
                ('price', models.FloatField()),
                ('stock', models.PositiveSmallIntegerField(default=0)),
                ('is_home', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlandi'), ('deleted', 'Silindi')], default='draft', max_length=10)),
                ('createt_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
