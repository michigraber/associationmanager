from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from associates.models import Associate


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(BaseModel):
    '''
    '''
    title_de = models.CharField(max_length=511)
    title_en = models.CharField(max_length=511)

    date_from = models.DateField()
    date_until = models.DateField()

    slug = models.SlugField(unique=True)

    description_de = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)

    schedule_de = models.TextField(blank=True, null=True)
    schedule_en = models.TextField(blank=True, null=True)

    show_event = models.BooleanField(default=True)

    event_part_set_price_map_json = models.CharField(max_length=255,
            blank=True, null=True)

    def __str__(self):
        return self.title_en


class EventPart(BaseModel):
    '''
    '''
    event = models.ForeignKey(Event)

    datetime_from = models.DateTimeField()
    datetime_until = models.DateTimeField()

    short_description_de = models.CharField(max_length=511)
    short_description_en = models.CharField(max_length=511)

    is_bookable = models.BooleanField()
    max_number_of_participants = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (
                ('event', 'short_description_en'),
                ('event', 'short_description_de')
                )

    def __str__(self):
        return self.event.title_en + ' : ' + self.short_description_en

    def no_eventparts_registered(self):
        return len(self.registration_set.all())

    def still_available(self):
        no_reg = self.no_eventparts_registered()
        return  no_reg < self.max_number_of_participants

    def percent_full(self):
        reg = float(self.no_eventparts_registered())
        maxav = float(self.max_number_of_participants)
        return int(100*reg/maxav)

    def no_available_places(self):
        return self.max_number_of_participants - self.no_eventparts_registered()


class Registration(BaseModel):
    '''
    '''
    associate = models.ForeignKey(Associate)
    event_parts = models.ManyToManyField(EventPart)
    price = models.PositiveSmallIntegerField(blank=True, null=True)

    def one_line_description(self, language='de'):
        if language == 'de':
            return 'Registration ({pk}) : {fn} {ln}'.format(
                    pk=self.pk,
                    fn=self.associate.first_name, ln=self.associate.last_name)
        elif language == 'en':
            return 'Registration ({pk}) : {fn} {ln}'.format(
                    pk=self.pk,
                    fn=self.associate.first_name, ln=self.associate.last_name)
        else:
            return 'Registration ({pk}) : {fn} {ln}'.format(
                    pk=self.pk,
                    fn=self.associate.first_name, ln=self.associate.last_name)

 
class Article(BaseModel):
    '''
    '''
    name_de = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    description_de = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    # FIXME : might come in handy at a later stage
#   article_image = models.ImageField(upload_to='articles', blank=True,
#           null=True)

    events = models.ManyToManyField(Event, blank=True, null=True)

    is_sold = models.BooleanField(default=True)
    price = models.PositiveSmallIntegerField()
    number_of_items_available = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.one_line_description()

    def one_line_description(self, language='de'):
        if language == 'de':
            return self.name_de
        elif language == 'en':
            return self.name_en
        else:
            return 'Article - no name in language %s' % language

    def no_articles_sold(self):
        pis = PurchaseItem.objects.filter(
                content_type__model='registration',
                object_id=self.pk)
        return len(pis)

    def still_available(self):
        return self.no_articles_sold() < self.number_of_items_available



class Purchase(BaseModel):
    '''
    '''
    associate = models.ForeignKey(Associate)
    message = models.TextField(blank=True, null=True)

    PAYMENT_STATUS_CHOICES = (
            (0, 'not paid yet'),
            (1, 'paid by cash'),
            (2, 'paid by paypal'),
            (4, 'paid by bank transfer'),
            )
    payment_status = models.SmallIntegerField(choices=PAYMENT_STATUS_CHOICES,
            default=0)
    payment_due_by = models.DateField(blank=True, null=True)

    def one_line_description(self):
        items = self.purchaseitem_set.all()
        s = 'Purchase Number {pk} :: '.format(pk=self.pk)
        if len(items) > 0:
            s += ', '.join([str(i.one_line_description())+\
                    ' ('+str(i.content_object.price)+'.-)'
                for i in items])
        else:
            s += 'Purchase without items!!'

        s += ' Balance due : {b}.- Payment: {p}'.format(
                b=self.balance_due(),
                p=self.get_payment_status_display())
        return s

    def balance_due(self):
        balance = 0
        for i in self.purchaseitem_set.all():
            balance += i.content_object.price
        return balance


class PurchaseItem(BaseModel):
    '''
    '''
    ITEM_TYPE_CHOICES = models.Q(app_label='events', model='article') |\
            models.Q(app_label='events', model='registration') 
    content_type = models.ForeignKey(generic.ContentType,
            limit_choices_to=ITEM_TYPE_CHOICES)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    purchase = models.ForeignKey(Purchase)

    @property
    def price(self):
        self.content_object.price

    def one_line_description(self, language='en'):
        return self.content_object.one_line_description(language=language)


