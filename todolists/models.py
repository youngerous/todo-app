from django.db import models
import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField('TITLE', max_length=50, blank=True)
    content = models.CharField('CONTENT', max_length=50, blank=True)
    deadline = models.IntegerField(default=0, blank=True)
    importance = models.IntegerField(default=0, blank=True)
    isFinished = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.title:
            self.title = 'Empty title'
        if not self.content:
            self.content = 'Empty content'
        if not self.importance:
            self.importance = 0
        if not self.deadline:
            self.deadline = 0
        if not self.isFinished:
            self.isFinished = 0
        
        super().save()