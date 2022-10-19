from django.contrib import admin

# Register your models here.
from .models import User, Osoba

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)

admin.site.register(User)
admin.site.register(Osoba,OsobaAdmin)