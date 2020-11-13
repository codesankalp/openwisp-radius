from django.db import migrations

from openwisp_radius.migrations import populate_phonetoken_phone_number


class Migration(migrations.Migration):

    dependencies = [
        ('sample_radius', '0005_phonetoken_phone_number'),
    ]

    operations = [
        migrations.RunPython(
            populate_phonetoken_phone_number, reverse_code=migrations.RunPython.noop
        ),
    ]
