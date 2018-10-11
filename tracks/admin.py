from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Track, Sender


@admin.register(Track, Sender)
class TrackModelAdmin(ImportExportModelAdmin):
    # fields = ['__all__']
    exclude = ['created', 'updated']
    # list_filter = ['complete']
    # prepopulated_fields = {'slug': ('title',), }



# admin.site.register(Sender)
