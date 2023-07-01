from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class ModelInline(admin.StackedInline):
    model = CarModel
    extra = 3

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [ModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)