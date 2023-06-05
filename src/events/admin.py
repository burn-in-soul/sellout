from django.contrib import admin

from events.models import Events


class EventsAdmin(admin.ModelAdmin):
    fields = (
        'name', 'description', 'tickets_link', 'vk_link', 'start_date',
        'end_date',
        'poster', 'image_tag')
    readonly_fields = ('image_tag',)
    ordering = ('-start_date',)
    list_display = ('name', 'start_date')


admin.site.register(Events, EventsAdmin)
