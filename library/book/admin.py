from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('titulo', 'valor', 'valoracion')
    list_filter = ('valoracion', 'fecha_modificacion')

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            (None, {
                'fields': ('titulo', 'autor', 'descripcion', 'valor', 'valoracion')
            }),
        ]
        if obj:  
            fieldsets.append(('Fechas', {
                'fields': ('fecha_creacion', 'fecha_modificacion'),
            }))
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return self.readonly_fields
        return () 