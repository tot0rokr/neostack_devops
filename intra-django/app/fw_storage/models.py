from django.db import models

# Create your models here.

class Nordic(models.Model):
    title = models.CharField(max_length=256)
    commit_hash = models.CharField(max_length=41, null=True)
    built_at = models.DateTimeField()
    committed_at = models.DateTimeField()
    # tags = models.CharField(max_length=64, blank=True, null=True)
    author = models.CharField(max_length=32, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fw_binary = models.FileField(upload_to='nordic_fw/', blank=True, null=True)
    # commit_message = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'#{self.pk}: {self.title}'

    def get_absolute_url(self):
        return f'/{self.pk}/'

