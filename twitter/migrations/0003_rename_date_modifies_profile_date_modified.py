from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_profile_date_modifies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='date_modifies',
            new_name='date_modified',
        ),
    ]
