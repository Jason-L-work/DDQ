# Generated by Django 5.2.3 on 2025-06-24 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DDQ', '0002_remove_surveyresponse_image_answer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('is_file_upload', models.BooleanField(default=False, help_text='Check if this question requires a file upload.')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Anonymous', max_length=200)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.RemoveField(
            model_name='surveyresponse',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='surveyresponse',
            name='name',
        ),
        migrations.RemoveField(
            model_name='surveyresponse',
            name='uploaded_file',
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, default='2025-06-24 08:00:00'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(blank=True, null=True)),
                ('file_answer', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='DDQ.surveyresponse')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DDQ.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='DDQ.survey'),
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DDQ.survey'),
            preserve_default=False,
        ),
    ]
