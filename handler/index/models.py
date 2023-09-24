from django.db import models


class Handler(models.Model):
    greeting = models.TextField()
    nickname = models.CharField(
        max_length=100
    )
    mail = models.CharField(
        max_length=20
    )


class SocialLink(models.Model):
    sitename = models.CharField(
        max_length=100
    )
    link = models.URLField()
    handler = models.ForeignKey(
        Handler,
        related_name='sitelinks',
        on_delete=models.CASCADE
    )
