from django.db import models


class Todo(models.Model):

    name = models.TextField()
    is_complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Todos"

    def __str__(self):
        return '{0}'.format(self.name)
