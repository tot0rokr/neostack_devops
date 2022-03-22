from django.db import models

# Create your models here.

class Nordic(models.Model):
    title = models.CharField(max_length=256)
    state = models.CharField(max_length=16, blank=True, null=True)
    commit_hash = models.CharField(max_length=41)
    built_at = models.DateTimeField()
    committed_at = models.DateTimeField()
    # tags = models.CharField(max_length=64, blank=True, null=True)
    author = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    fw_binary = models.FileField(upload_to='nordic_fw/', blank=True, null=True)
    # commit_message = models.TextField(blank=True, null=True)


    def __str__(self):
        if self.state is not None and self.state != '':
            return f'{self.title}'
        else:
            return f'{self.title}'

    def get_absolute_url(self):
        return f'/{self.pk}/'

