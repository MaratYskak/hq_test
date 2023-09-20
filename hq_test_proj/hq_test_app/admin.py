from django.contrib import admin
from .models import Product, Lesson, LessonView

# Регистрируем модели в админке
admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(LessonView)
