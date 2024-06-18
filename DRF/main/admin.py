from django.contrib import admin

from .models import Bank, Currency, Exchange


# Register your models here.
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'UNN')
    list_display_links = ('id', 'name', 'UNN')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency_name', 'slug')
    list_display_links = ('id', 'currency_name', 'slug')

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency_exchange', 'data', 'bank', 'currency')
    list_display_links = ('id', 'currency_exchange', 'data', 'bank', 'currency')