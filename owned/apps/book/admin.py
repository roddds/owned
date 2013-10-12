from django.contrib import admin
from django.db import models
from book.models import Paragraph, Option

class OptionAdmin(admin.StackedInline):
    model = Option

class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_text')

    inlines = [OptionAdmin,]


admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(Option)

