from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class Ticket(models.Model):
    title = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        max_length=500,
        blank=True,
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        null=True,
        blank=True,
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
    )


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
    )

    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by',

    )

    class Meta:
        unique_together = ('user',
                           'followed_user',)


class Review(models.Model):
    ticket = models.ForeignKey(
        to=Ticket,
        on_delete=models.CASCADE,
    )

    rating = models.PositiveSmallIntegerField(
        # max_length=1024,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
    )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    headline = models.CharField(
        max_length=200,
    )

    body = models.TextField(
        max_length=500,
        blank=True,
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
    )


class Account(AbstractUser):
    pass
