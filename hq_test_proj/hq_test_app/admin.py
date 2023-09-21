from django.contrib import admin
from .models import Product, Lesson, LessonView
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(LessonView)
class LessonViewModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "lesson",
        "viewed_time_seconds",
        "viewed"
    )
    exclude = ('viewed',)

@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
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
