# Generated by Django 4.2.4 on 2023-08-29 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0002_workspace_deleted_at_workspace_is_deleted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workspace',
            old_name='members',
            new_name='member',
        ),
    ]
