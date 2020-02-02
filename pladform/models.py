import datetime
from django.db.models import Q
from django.db.models import F
from django.urls import reverse
from django.db import models
from django.utils import timezone
from rest_framework.reverse import reverse as api_reverse

# class ActionWithModels(models.Model):
#     model = models.ForeignKey()
#     count = models.PositiveIntegerField(default=0)


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    objects = models.Manager()

    def get_api_url(self, request=None):
        return api_reverse('pladform_api:blogs_rud', kwargs={'pk': self.pk}, request=request)

    def get_absolute_url(self):
        return reverse('pladform_api:blogs_rud', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class EntryQuerySet(models.QuerySet):
    def with_comments_greater(self, number):
        return self.filter(number_of_comments__gte=number)

    def with_rating_greater(self, number):
        return self.filter(rating__gte=number)


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(null=True, blank=True)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.headline

    def was_published_recently(self):
        return self.pub_date >= timezone.now().date() - datetime.timedelta(days=1)


class SubscriptionQuerySet(models.QuerySet):
    def get_active_subscriptions_by_date(self, date: datetime.date) -> 'SubscriptionQuerySet':
        return self.filter(end_date__gte=date, start_date__lte=date, start_date__gt=F('end_date'))

    def get_active_subscriptions_by_date_range(
            self,
            date_from: datetime.date,
            date_to: datetime.date,
    ) -> 'SubscriptionQuerySet':
        return self.filter(Q(end_date__gte=date_from) | Q(start_date__lte=date_to))


class Subscription(models.Model):
    start_date = models.DateField('Дата активации')
    end_date = models.DateField('Дата окончания (включительно)')
    client = models.ForeignKey(Author, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)

    objects = SubscriptionQuerySet.as_manager()



"""
Напишите функцию (или что-то еще), которая принимает на вход дату (день)
и возвращает все подписки, активные в этот день.
"""
