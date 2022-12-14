# Generated by Django 4.1.1 on 2022-09-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_ownercertificate_ownerclient_ownerexpertat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_certificate',
            field=models.ManyToManyField(to='owner.ownercertificate', verbose_name='owner certificate'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_client',
            field=models.ManyToManyField(to='owner.ownerclient', verbose_name='owner client'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_experience_detail',
            field=models.ManyToManyField(to='owner.ownerexperiencedetail', verbose_name='owner experience detail'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_expert_at',
            field=models.ManyToManyField(to='owner.ownerexpertat', verbose_name='owner expert at'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_knowledge',
            field=models.ManyToManyField(to='owner.ownerknowledge', verbose_name='owner knowledge'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_testimonial',
            field=models.ManyToManyField(to='owner.ownertestimonial', verbose_name='owner testimonial'),
        ),
        migrations.AlterField(
            model_name='ownerresumesubject',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='name'),
            preserve_default=False,
        ),
    ]
