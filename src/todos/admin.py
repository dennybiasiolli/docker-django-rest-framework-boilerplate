from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dati principali', {
            'fields': [
                'name',
                'is_complete',
            ],
        }),
        ('Data creazione e ultima modifica', {
            'fields': (
                'created_date',
                'modified_date',
            ),
        }),
    ]
    readonly_fields = ('created_date', 'modified_date',)
    list_display = ('name', 'is_complete',
                    'created_date', 'modified_date')
    list_filter = (
        'is_complete',
        'created_date',
        'modified_date',
    )
    search_fields = ['name']


admin.site.register(Todo, TodoAdmin)
