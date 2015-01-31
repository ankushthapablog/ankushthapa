from django.db import models

class AccessLogs(models.Model):
    access_string = models.CharField(verbose_name='access string', null=True, blank=True, max_length=200)
    page_name = models.CharField(verbose_name="page name", null=True, blank=True, max_length=100)

    def __unicode__(self):
        return self.access_string
