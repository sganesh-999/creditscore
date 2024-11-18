from django.contrib import admin
from .models import *
#Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra =1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)