from django.contrib import admin
from .models import Product, Lesson, LessonView



@admin.register(LessonView)
class LessonViewModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "lesson",
        "viewed_time_seconds",
        "viewed"
    )

@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "video_link",
        "duration_seconds",
    )

@admin.register(Product)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
    )
