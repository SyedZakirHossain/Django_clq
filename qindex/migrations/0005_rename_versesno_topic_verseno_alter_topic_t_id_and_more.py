# Generated by Django 4.1.7 on 2023-03-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qindex', '0004_t_list_delete_img_remove_topic_topicno_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='versesno',
            new_name='verseno',
        ),
        migrations.AlterField(
            model_name='topic',
            name='t_id',
            field=models.CharField(max_length=500),
        ),
        migrations.DeleteModel(
            name='t_list',
        ),
    ]
