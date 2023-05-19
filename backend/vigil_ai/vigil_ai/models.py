from django.db import models

class Email(models.Model):
    email_address = models.EmailField()
    email_body = models.TextField()
    is_scam = models.BooleanField()

    def __str__(self):
        return self.email_address
