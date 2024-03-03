from django.contrib import admin
from .models import Idea, Comment
from django.utils.html import format_html


class CommentInLine(admin.StackedInline):
    model = Comment


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'status', 'show_url']
    list_filter = ['status']
    inlines = [
        CommentInLine
    ]

    def show_url(self, obj):
        if obj.websites is not None:
            return format_html(f'<a href="{obj.websites}" target="_blank">{obj.websites}</a>')
        else:
            return ''

    show_url.short_description = 'Website URL'


@admin.register(Comment)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']
