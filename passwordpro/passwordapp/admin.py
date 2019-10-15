from django.contrib import admin
from .models import Register
from django.http import HttpResponse

admin.site.site_header = 'Mani Kumar'


class Registeradmin(admin.ModelAdmin):
    list_display = ('email','password')
    list_filter = ('email',)
    search_fields = ('email',)

admin.site.register(Register,Registeradmin)