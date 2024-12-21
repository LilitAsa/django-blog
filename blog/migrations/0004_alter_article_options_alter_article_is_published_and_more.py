# Generated by Django 4.2.15 on 2024-12-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['time_create']},
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=1, verbose_name=[(0, 'Draft'), (1, 'Published')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['time_create'], name='blog_articl_time_cr_d1612f_idx'),
        ),
    ]