from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AssociateGroup(BaseModel):
    '''
    examples:
    - aikikai member
    - receives aikikai newsletter
    - receives ikeda seminar newsletter
    '''
    name = models.CharField(max_length=64) 
    description = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name


class Associate(BaseModel):
    '''
    '''
    user = models.OneToOneField(User, blank=True, null=True)

    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    LANGUAGE_GERMAN = 0
    LANGUAGE_ENGLISH = 1
    LANGUAGE_CHOICES = (
            (LANGUAGE_GERMAN, 'de'),
            (LANGUAGE_ENGLISH, 'en'),
            )
    language = models.PositiveSmallIntegerField(choices=LANGUAGE_CHOICES,
            blank=True, null=True)

    RANK_CHOICES = (
            (0, 'no rank yet'), (1, '6th Kyu'), (2, '5th Kyu'), (3, '4th Kyu'),
            (4, '3rd Kyu'), (5, '2nd Kyu'), (6, '1st Kyu'), (7, '1st Dan'),
            (8, '2nd Dan'), (9, '3rd Dan'), (10, '4th Dan'), (11, '5th Dan'),
            (12, '6th Dan'), (13, '7th Dan'), (14, '8th Dan'), (15, '9th Dan'),
            (16, '10th Dan'),
            )

    rank = models.PositiveSmallIntegerField(choices=RANK_CHOICES, null=True,
            blank=True)
    member_since = models.DateField(blank=True, null=True)

    is_organization_contact = models.BooleanField(default=False)
    organization = models.CharField(max_length=128, blank=True, null=True)
    street_and_nr = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    postal_code = models.CharField(max_length=16, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)

    phone_number_home = models.CharField(max_length=128, blank=True,
            null=True)
    phone_number_mobile = models.CharField(max_length=128, blank=True,
            null=True)
    phone_number_business = models.CharField(max_length=128, blank=True,
            null=True)

    email_address = models.EmailField(max_length=75, blank=True, null=True)

    # emergency contact
    emergency_contact_first_name = models.CharField(max_length=128, blank=True,
            null=True)
    emergency_contact_last_name = models.CharField(max_length=128,
            blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=128,
            blank=True, null=True)
    emergency_contact_phone_number = models.CharField(max_length=128,
            blank=True, null=True)
    emergency_contact_email_address = models.EmailField(max_length=75,
            blank=True, null=True)
    
    group_memberships = models.ManyToManyField(AssociateGroup,
            related_name='associate_groups', blank=True, null=True)

#   class Meta:
#       unique_together = (
#               ('first_name', 'last_name', 'email_address', ),
#                   )

    def __unicode__(self):
        return u'%s, %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        # overwrite to make emailfield unique if not null according to
        # http://stackoverflow.com/questions/15422606/
        #django-model-email-field-unique-if-not-null-blank
        if self.email_address == "":
            self.email_address = None
        super(Associate, self).save(*args, **kwargs)

    def pretty_print_basic(self):
        s = self.first_name + ' ' + self.last_name + '\n'
        s += self.street_and_nr + '\n'
        s += self.postal_code + ' ' + self.city + '\n'
        s += self.country + '\n'
        return s.encode('utf-8')
