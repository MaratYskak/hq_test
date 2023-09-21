from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')

class LessonView(models.Model):
    """
    отслеживает просмотр уроков пользователями
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    viewed_time_seconds = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Проверяем, насколько процентов просмотрен урок
        if self.viewed_time_seconds >= (self.lesson.duration_seconds * 0.8):
            self.viewed = True
        else:
            self.viewed = False

        super().save(*args, **kwargs)
