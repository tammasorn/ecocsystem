from django.contrib import admin
from .models import ModelRegister,Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","email","telephone_number"]
    search_fields = ["first_name","last_name","telephone_number"]

    class Meta:
        model= Register


admin.site.register(ModelRegister)
admin.site.register(Register,RegisterAdmin)