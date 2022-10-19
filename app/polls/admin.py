from django.contrib import admin

# Register your models here.
from .models import User, Osoba, Druzyna

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania']
class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']

admin.site.register(User)
admin.site.register(Osoba,OsobaAdmin)
admin.site.register(Druzyna,DruzynaAdmin)
