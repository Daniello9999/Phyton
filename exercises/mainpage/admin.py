from django.contrib import admin
from maths.models import Math
# Register your models here.

class MathAdmin(admin.ModelAdmin):
    pass

admin.site.register(Math, MathAdmin)