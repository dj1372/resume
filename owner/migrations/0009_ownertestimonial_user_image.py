# Generated by Django 4.1.1 on 2022-09-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0008_alter_owner_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownertestimonial',
            name='user_image',
            field=models.ImageField(blank=True, default='testimonial-default.jpg', upload_to='testimonials', verbose_name='testimonial user image'),
        ),
    ]