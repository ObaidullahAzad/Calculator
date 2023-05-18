from django.contrib import admin
from dynamic.models import Dynamic
class DynamicAdmin(admin.ModelAdmin):
    list_display=('First','Last','Email','Password')

admin.site.register(Dynamic,DynamicAdmin)

# Register your models here.
