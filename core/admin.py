from django.contrib import admin

from core.models import ActivityLog, Filme


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'status', 'imagem', 'categoria')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Filme, FilmeAdmin)
