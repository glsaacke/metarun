# Generated by Django 5.1.1 on 2024-09-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_activity_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=100)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('isPublished', models.BooleanField(default=False)),
                ('order', models.IntegerField()),
            ],
        ),
    ]
