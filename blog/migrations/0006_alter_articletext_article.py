# Generated by Django 4.1.7 on 2023-04-02 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_articletext_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletext',
            name='article',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articletext', to='blog.article'),
        ),
    ]