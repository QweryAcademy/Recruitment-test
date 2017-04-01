# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser, UserManager
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

class GClass(models.QuerySet):
        def with_bookings(self):
            result = [user.pk for user in self.all() if user.orders.count() > 0]
           # for user in self.all():
            #    if user.orders.count() > 0 
             #   result.append(user)
            return self.filter(pk__in=result)
        
        def with_transaction_total(self):
            result = []
            for user in self.all():
                if hasattr(user, 'wallet'):
                    result.append(user.pk)
            return self.filter(pk__in=result)

        def with_transaction_and_booking(self):
            result = []
            for user in self.all():
                if (hasattr(user, 'wallet' )) & (user.orders.count() > 0):
                    result.append(user.pk)
            return self.filter(pk__in=result)

        def no_bookings(self):
               
            #Entry.objects.filter(pub_date__isnull=True)
            return self.filter(orders__isnull=True).reverse()


    #import pdb; pdb.set_trace()
    #return self


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    g_objects = GClass().as_manager()

    
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    # @property
    # def transaction_total(self):
    #     if not hasattr(self, 'wallet'):
    #         Wallet.objects.create(owner=self)
    #     result = self.wallet.transactions.aggregate(total=models.Sum('total'))
    #     return result['total'] or 0

class Booking(models.Model):
    user = models.ForeignKey(User, null=True, related_name='orders')
    order = models.CharField(max_length=12, primary_key=True, db_index=True)


class Wallet(models.Model):
    owner = models.OneToOneField(User, related_name='wallet')


class WalletTransaction(models.Model):
    wallet = models.ForeignKey(Wallet, related_name='transactions')
    booking = models.ForeignKey(Booking, null=True)
    total = models.DecimalField(decimal_places=2, max_digits=10)
