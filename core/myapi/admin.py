from django.contrib import admin
from .models import website, linkapi


class PageWeb(admin.ModelAdmin):
    list_display = ('id_web','nama','link','user','deskripsi','date_created')
    list_display_links = ('id_web','nama','link','user','deskripsi','date_created')
    search_fields = ('id_web','nama','link','user','deskripsi','date_created')
    list_per_page = 10

class PageApi(admin.ModelAdmin):
    list_display = ('user','id_link','link_web','urlapi')
    list_display_links = ('user','id_link','link_web','urlapi')
    search_fields = ('user','id_link','link_web','urlapi')
    list_per_page = 10


admin.site.register(website, PageWeb)
admin.site.register(linkapi, PageApi)
