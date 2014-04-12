from django.db import models
from django.contrib.auth.models import User


class AssociateGroup(models.Model):
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


class Associate(models.Model):
    '''
    '''
    user = models.OneToOneField(User, blank=True, null=True)

    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)

    is_organization_contact = models.BooleanField(default=False)
    organization = models.CharField(max_length=128, blank=True, null=True)
    street_and_nr = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    postal_code = models.CharField(max_length=16, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)

    phone_number = models.CharField(max_length=128, blank=True, null=True)
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
            related_name='associate_groups')

    def __unicode__(self):
        return u'%s, %s' % (self.first_name, self.last_name)
