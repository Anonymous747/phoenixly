# Generated by Django 4.2 on 2023-07-03 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0002_document_related_folder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_collection', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='document',
            name='related_folder',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='parent_collection_id',
        ),
        migrations.AddField(
            model_name='document',
            name='related_folder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_related_folder', to='library.folder'),
        ),
        migrations.AddField(
            model_name='folder',
            name='parent_collection_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folders_parent_collection', to='library.collection'),
        ),
    ]
