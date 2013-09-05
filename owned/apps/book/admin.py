from django.contrib import admin
from book.models import Paragraph, Option


class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_text')


admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(Option)