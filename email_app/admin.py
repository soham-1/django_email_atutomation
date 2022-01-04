from django.contrib import admin
from .models import EmailModel

# Register your models here.

class EmailAdmin(admin.ModelAdmin):
    readonly_fields = ('send_time',)

admin.site.register(EmailModel, EmailAdmin)