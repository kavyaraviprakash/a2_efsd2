from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    is_customer = models.BooleanField('customer', default=True)
    is_FinancialAdvisor = models.BooleanField('FinancialAdvisor', default=False,
                                              help_text='check it if you want to sign up as Financial Advisor')

    def __str__(self):
        return '{}'.format(self.username)
