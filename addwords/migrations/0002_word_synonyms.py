# Generated by Django 3.2.16 on 2023-02-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addwords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='synonyms',
            field=models.ManyToManyField(related_name='_addwords_word_synonyms_+', to='addwords.Word', verbose_name='Синонимы'),
        ),
    ]
