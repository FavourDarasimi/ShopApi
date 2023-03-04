# Generated by Django 4.1.7 on 2023-02-25 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartSession', models.CharField(max_length=200)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paymentMethod', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.cart')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imageUrl', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('billingAddress', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='billing_address', to='account.address')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.cart')),
                ('shippingAddress', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='shipping_address', to='account.address')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.product')),
            ],
        ),
    ]
