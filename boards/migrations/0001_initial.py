# Generated by Django 4.2.4 on 2023-08-14 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspaces', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='title of board', max_length=50, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='description of board activities (optional)', null=True, verbose_name='Description')),
                ('background_image', models.FileField(blank=True, null=True, upload_to='uploads/photos')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to=settings.AUTH_USER_MODEL, verbose_name='Board Owner')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='workspaces.workspace', verbose_name='Workspace')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(max_length=50)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='boards.board')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='enter the title', max_length=50, verbose_name='Title')),
                ('order', models.DecimalField(blank=True, decimal_places=6, max_digits=7, null=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='boards.board')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='title of task', max_length=50, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='describe your task (optional)', null=True, verbose_name='Description')),
                ('deadline', models.DateTimeField(blank=True, help_text='specify a deadline (optional)', null=True, verbose_name='Deadline')),
                ('start_date', models.DateTimeField(blank=True, help_text='date of start doing task (optional)', null=True, verbose_name='Start Date')),
                ('finished_date', models.DateTimeField(blank=True, help_text='date of when the task finished (optional)', null=True, verbose_name='Finish Date')),
                ('time_spent', models.TimeField(blank=True, help_text='the time you spent for doing this task (optional)', null=True, verbose_name='Time Spent')),
                ('order', models.DecimalField(blank=True, decimal_places=6, max_digits=7, null=True)),
                ('board_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='boards.list', verbose_name='List')),
                ('label', models.ManyToManyField(related_name='tasks', to='boards.label', verbose_name='Label')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(blank=True, help_text='enter the comment', max_length=200, null=True, verbose_name='Comment')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='boards.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]