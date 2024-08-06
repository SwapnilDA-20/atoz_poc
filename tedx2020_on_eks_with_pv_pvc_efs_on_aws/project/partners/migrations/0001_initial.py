# Generated by Django 2.2.6 on 2019-11-06 17:41

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_type', models.CharField(choices=[('GS', 'Grand Sponsors'), ('GCS', 'Grand Carrier Sponsors'), ('GHS', 'Grand Hospitality Sponsors'), ('SPO', 'Sponsors'), ('SUP', 'Supporters'), ('MP', 'Media Partners'), ('CP', 'Community Partners')], max_length=3)),
                ('link', models.URLField()),
                ('image', versatileimagefield.fields.VersatileImageField(height_field='image_height', upload_to='partners/', verbose_name='Image', width_field='image_width')),
                ('image_height', models.PositiveIntegerField(editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(editable=False, null=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PartnerTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='partners.Partner')),
            ],
            options={
                'verbose_name': 'partner Translation',
                'db_table': 'partners_partner_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
