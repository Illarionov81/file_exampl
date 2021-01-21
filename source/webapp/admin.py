from django.contrib import admin

from webapp.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'author', 'upload_date',)


admin.site.register(File, FileAdmin)

