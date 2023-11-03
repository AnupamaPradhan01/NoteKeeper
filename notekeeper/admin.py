from django.contrib import admin
from notekeeper.models import Notekeeper

@admin.register(Notekeeper)
class NotekeeperAdmin(admin.ModelAdmin):
    list_display=('title','description')
