from django.contrib import admin

from typeidea.BaseOwnerAdmin import BaseOwnerAdmin
from .models import Link, SideBar


@admin.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    # list_page
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    # edit_page
    fields = ('title', 'href', 'status', 'weight')


@admin.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    # list_page
    list_display = ('title', 'display_type', 'content', 'created_time')
    # edit_page
    fields = ('title', 'display_type', 'content')