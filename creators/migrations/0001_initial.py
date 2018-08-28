# Generated by Django 2.0 on 2018-08-09 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatorProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField()),
                ('audience_demographic', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('offering', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('platform', models.CharField(choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram'), ('Pinterest', 'Pinterest'), ('Blog', 'Blog'), ('YouTube', 'YouTube')], max_length=65)),
                ('account_name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('metrics', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creators.CreatorProfile')),
            ],
        ),
    ]