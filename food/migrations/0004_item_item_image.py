# Generated by Django 4.2.11 on 2024-03-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0003_remove_item_item_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://www.google.kz/imgres?imgurl=https%3A%2F%2Flivingstonbagel.com%2Fwp-content%2Fuploads%2F2016%2F11%2Ffood-placeholder.jpg&tbnid=Ag1_-7HSofts3M&vet=12ahUKEwjz6M7w-_CEAxVv2rsIHSJWBlQQMygYegUIARCHAQ..i&imgrefurl=https%3A%2F%2Fwww.everestkitchenpa.com%2Fassets%2Fpages%2Fseafood.html&docid=CjxME5QfBnvVSM&w=499&h=374&q=placeholder%20food%20image&ved=2ahUKEwjz6M7w-_CEAxVv2rsIHSJWBlQQMygYegUIARCHAQ",
                max_length=500,
            ),
        ),
    ]
