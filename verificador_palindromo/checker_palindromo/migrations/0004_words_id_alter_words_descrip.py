# Generated by Django 4.2.5 on 2023-09-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker_palindromo', '0003_remove_words_is_palindrome'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='words',
            name='descrip',
            field=models.CharField(max_length=20),
        ),
    ]