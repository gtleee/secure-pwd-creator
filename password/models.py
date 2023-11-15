from django.db import models

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='IP Address')
    session_key = models.CharField(max_length=40, verbose_name='Session Key', blank=True, null=True)
    referer = models.TextField(verbose_name='HTTP Referer', blank=True, null=True)
    status_code = models.PositiveIntegerField(verbose_name='HTTP Status Code', blank=True, null=True)
    user_agent = models.CharField(max_length=255, verbose_name='User Agent', blank=True)
    page_path = models.CharField(max_length=2048, verbose_name='Page Path', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return f'{self.ip_address} visited at {self.timestamp}'
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'