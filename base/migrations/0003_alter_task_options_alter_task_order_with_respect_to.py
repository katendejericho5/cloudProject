# Generated by Django 4.2.1 on 2023-05-13 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_auto_20210322_2234"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["user"]},
        ),
        migrations.AlterOrderWithRespectTo(
            name="task",
            order_with_respect_to=None,
        ),
    ]