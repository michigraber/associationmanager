from django.db import models



class Event(models.model):
    '''
    '''
    title = models.CharField(max_length=511)
    date_from = models.DateField()
    date_until = models.DateField()
    description = models.TextField()
    schedule = models.TextField()

    show_event = models.BooleanField(default=True)


class EventPart(models.model):
    '''
    '''
    event = models.ForeignKey(Event)

    datetime_from = models.DateTimeField()
    datetime_until = models.DateTimeField()

    short_description = models.CharField(max_length=511)

    is_bookable = models.BooleanField()
    price_sfr = models.PositiveSmallIntegerField()
    max_number_of_participants = models.PositiveSmallIntegerField()


class Registration(models.models):
    '''
    '''
    event_parts = models.ManyToManyRelationshipField(EventPart)
    total_price = model.PositiveSmallIntegerField()

    
class Item(models.model):
    '''
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()

    is_sold = models.BooleanField()
    price_sfr = models.PositiveSmallIntegerField()
    number_of_items = models.PositiveSmallIntegerField()


class Purchase(models.model):
    '''
    '''
    member = models.ForeignKey(Member)
    # XXX 
    ITEM_TYPE_CHOICES = models.Q(app_label='member', model='item') |\
            models.Q(app_label='member', model='registration') 
    object_type = models.ForeignKey(generic.ContentType, 
            limit_choices_to=ITEM_TYPE_CHOICES)
    
    item = models.GenericRelationField(EventPurchase)

    is_paid = models.BooleanField()

    comment = models.TextField()





