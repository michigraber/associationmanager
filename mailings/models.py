from django.db import models

class Mailing(models.model):
    '''
    '''
    subject = models.CharField(max_length=511)
    content = models.TextField()

    addressee_group = models.ForeignKey(MemberGroup)

