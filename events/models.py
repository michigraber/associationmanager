from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from associates.models import Associate



class Event(models.Model):
    '''
    '''
    title_de = models.CharField(max_length=511)
    title_en = models.CharField(max_length=511)

    date_from = models.DateField()
    date_until = models.DateField()

    slug = models.SlugField()

    description_de = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)

    schedule_de = models.TextField(blank=True, null=True)
    schedule_en = models.TextField(blank=True, null=True)

    show_event = models.BooleanField(default=True)

    event_part_set_price_map_json = models.CharField(max_length=255)


class EventPart(models.Model):
    '''
    '''
    event = models.ForeignKey(Event)

    datetime_from = models.DateTimeField()
    datetime_until = models.DateTimeField()

    short_description_de = models.CharField(max_length=511)
    short_description_en = models.CharField(max_length=511)

    is_bookable = models.BooleanField()
    max_number_of_participants = models.PositiveSmallIntegerField()


class Registration(models.Model):
    '''
    '''
    associate = models.ForeignKey(Associate)
    event_parts = models.ManyToManyField(EventPart)
    price = models.PositiveSmallIntegerField(blank=True, null=True)
    PAID_BY_CHOICES = (
            (0, 'not paid'),
            (1, 'cash'),
            (2, 'paypal'),
            (4, 'bank transfer'),
            )
    paid_by = models.SmallIntegerField(choices=PAID_BY_CHOICES)

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

 
class Article(models.Model):
    '''
    '''
    name_de = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    description_de = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    article_image = models.ImageField(upload_to='articles', blank=True,
            null=True)

    events = models.ManyToManyField(Event, blank=True, null=True)

    is_sold = models.BooleanField(default=True)
    price = models.PositiveSmallIntegerField()
    number_of_items_available = models.PositiveSmallIntegerField()

    def one_line_description(self, language='de'):
        if language == 'de':
            return self.name_de
        elif language == 'en':
            return self.name_en
        else:
            return 'Article - no name in language %s' % language


class Purchase(models.Model):
    '''
    '''
    associate = models.ForeignKey(Associate)
    is_paid = models.BooleanField()
    comment = models.TextField(blank=True, null=True)

#   def __str__(self):
#       items = self.purchaseitem_set.all()
#       if len(items) > 0:
#           s = '\n'.join([str(i.one_line_description)+'\t'+str(i.price)+'.-'
#               for i in items])
#       else:
#           s = 'Purchase without items!!'
#       return s


class PurchaseItem(models.Model):
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


