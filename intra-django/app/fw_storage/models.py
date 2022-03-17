from django.db import models

# Create your models here.

class Nordic(models.Model):
    title = models.CharField(max_length=256)
    built_at = models.DateTimeField()
    committed_at = models.DateTimeField()
    commit_message = models.TextField(blank=True)
    tag = models.CharField(max_length=64, blank=True)
    binary = models.FileField(upload_to='nordic_fw/')


    def __str__(self):
        return f'#{self.pk}: {self.title}'

    def get_absolute_url(self):
        return f'/{self.pk}/'

