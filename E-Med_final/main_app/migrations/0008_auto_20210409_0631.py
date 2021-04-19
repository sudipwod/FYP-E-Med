# Generated by Django 3.0.3 on 2021-04-09 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200118_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalname', models.CharField(default='', max_length=50)),
                ('hospitaladd', models.CharField(default='', max_length=50)),
                ('hospitalphone', models.CharField(default='', max_length=50)),
                ('hospitalmap', models.CharField(default='', max_length=50)),
                ('hospitaltime', models.DateField(default='', max_length=50)),
                ('hospitalspecial', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='remedies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remedyname', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('remedydesc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='rating_review',
        ),
    ]
