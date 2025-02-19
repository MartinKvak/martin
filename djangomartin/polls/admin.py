from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):  # Používame ModelAdmin, nie TabularInline
    search_fields = ["question_text"]
    list_filter = ["pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]  # Opravené duplicitné list_display
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)  # Registrujeme správnu administrátorskú triedu
