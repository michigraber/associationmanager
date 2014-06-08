from datetime import timedelta
from django.utils.timezone import now

from .. import models

def delete_purchase(purchase_pk):
    '''
    Delete a purchase object and all its associated purchase items and
    registrations.
    '''
    purchase = models.Purchase.objects.get(pk=purchase_pk)
    purchase_items = purchase.purchaseitem_set.all()
    for pi in purchase_items:
        if type(pi.content_object) == models.Article:
             pi.delete()
        elif type(pi.content_object) == models.Registration:
            pi.content_object.delete()
            pi.delete()
    purchase.delete()
    return


def purchases_cleanup_payment_status_due_by():
    '''
    '''
    allpurs = models.Purchase.objects.all()
    for p in allpurs:
        if not p.payment_due_by:
            continue
        print p
        print p.payment_due_by
        print p.payment_due_by + timedelta(1)
        print now().date()
        print p.payment_status
        if p.payment_due_by + timedelta(1) < now().date() and\
                p.payment_status == models.Purchase.PENDING_PAYMENT_STATUS:
            p.payment_status = models.Purchase.EXPIRED_PAYMENT_STATUS
            print 'Purchase Item set elapsed, pk = ', p.pk
            p.payment_due_by = None
        elif p.payment_status != models.Purchase.PENDING_PAYMENT_STATUS:
            p.payment_due_by = None
        p.save()
