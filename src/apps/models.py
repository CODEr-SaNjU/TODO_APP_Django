from django.db import models

# Create your models here.

class TodoApp(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)


    class Meta:
        verbose_name = ('TODO')
        verbose_name_plural = ('TODO')

    def __str__(self):
        return self.title