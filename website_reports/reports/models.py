from django.db import models

class Report(models.Model):
    url = models.URLField()
    status_code = models.IntegerField(null=True, blank=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    date_retrieved = models.DateTimeField(auto_now=True)
    virus_total_details = models.JSONField(default=dict, blank=True)
    is_malicious = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.url} - {self.status_code}"
