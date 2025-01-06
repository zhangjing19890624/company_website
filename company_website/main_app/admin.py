from django.contrib import admin
from .models import NewsType, News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at')
    list_filter = ('type', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-order','-created_at')

admin.site.register(NewsType)
admin.site.register(News,NewsAdmin)