from django.test import TestCase

# Create your tests here.
import datetime
import pytest
from pladform.models import *

subscriptions_dates = [
    {
        'start_date':  datetime.datetime.strptime('January 1, 2020', '%B %d, %Y'),
        'end_date': datetime.datetime.strptime('January 10, 2020', '%B %d, %Y'),
    },
    {
        'start_date':  datetime.datetime.strptime('January 10, 2020', '%B %d, %Y'),
        'end_date': datetime.datetime.strptime('January 15, 2020', '%B %d, %Y'),
    }, {
     'start_date':  datetime.datetime.strptime('January 15, 2020', '%B %d, %Y'),
        'end_date': datetime.datetime.strptime('January 25, 2020', '%B %d, %Y'),
    }]


def setup():
    for subscription_dates in subscriptions_dates:
        Subscription.objects.create(**subscription_dates)


def test_get_active_subscriptions_by_date_range(date_from: datetime.date, date_to: datetime.date) -> None:
    subscriptions = Subscription.objects.all()
    excpted_first_casse = subscriptions[0]
    excpted_second_case = subscriptions[1]
    excpted_third_case = subscriptions[2]

    assert Subscription.objects.get_active_subscriptions_by_date_range(date_to, date_from)[0] == excpted_first_casse
    assert Subscription.objects.get_active_subscriptions_by_date_range(date_to, date_from)[0] == excpted_second_case
    assert Subscription.objects.get_active_subscriptions_by_date_range(date_to, date_from)[0] == excpted_third_case

