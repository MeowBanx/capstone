# Generated by Django 2.2 on 2019-05-17 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EditingProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('orig_file', models.FileField(blank=True, null=True, upload_to='textfile/')),
                ('orig_text', models.TextField(default='')),
                ('description', models.CharField(max_length=500)),
                ('turnaround', models.BooleanField(default='False')),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('edit_file', models.FileField(blank=True, null=True, upload_to='textfile/')),
                ('edit_text', models.TextField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('final_date', models.DateTimeField(blank=True, null=True)),
                ('word_count', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('submitted', models.BooleanField(default='False')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='brevisapp.ClientProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('reply', models.TextField(default='')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brevisapp.EditingProject')),
            ],
        ),
        migrations.CreateModel(
            name='EditorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='editingproject',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='brevisapp.EditorProfile'),
        ),
    ]
