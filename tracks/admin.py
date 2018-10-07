from django.contrib import admin


from .models import Track, Sender


@admin.register(Track)
class TrackModelAdmin(admin.ModelAdmin):
    # fields = ['__all__']
    exclude = ['created', 'updated']
    # prepopulated_fields = {'slug': ('title',), }


admin.site.register(Sender)
