from django.contrib import admin
from .models import Letter


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ['uppercase', 'lowercase', 'category', 'pronunciation_in_slovak', 'order']
    list_filter = ['category']
    search_fields = ['name', 'uppercase', 'lowercase']
    ordering = ['order']

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'uppercase', 'lowercase', 'order')
        }),
        ('Classification', {
            'fields': ('category',)
        }),
        ('Pronunciation', {
            'fields': ('pronunciation_in_slovak', 'pronunciation')
        }),
    )