from django.contrib.auth.models import User
from django.contrib import admin
from associates import models

class AssociateAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email_address', 'date_created')
    ordering = ('last_name', 'first_name',)

    list_filter = ('group_memberships', )

    fieldsets = (
        (None, {
            'fields': (('first_name', 'last_name', ),
                ('rank', 'date_of_birth', 'member_since',),
                ('email_address', 'phone_number_home', 'phone_number_mobile',
                    'phone_number_business')), }),
        (None, {
            'fields': ('user',),
        }),
        ('Mail Address', {
            'fields': (( 'organization', 'is_organization_contact',),
                'street_and_nr', 
                'postal_code',
                'city', 
                'country',),
            }),
        ('Group Memberships', {
            #'classes': ('collapse',),
            'fields': ('group_memberships',)
        }),
        ('Emergency Contact', {
            'classes': ('collapse',),
            'fields': (('emergency_contact_first_name',
                'emergency_contact_last_name', ),
                'emergency_contact_relationship',
                'emergency_contact_phone_number',
                'emergency_contact_email_address',)
        }),
        ('Log', {
            'fields': (('date_created', 'date_last_modified'),)
        }),
    )

    search_fields = ('first_name', 'last_name',
            'email_address', )

    readonly_fields = ('date_created', 'date_last_modified', )

    #list_editable = ('email_address', )

admin.site.register(models.Associate, AssociateAdmin)

        
class AssociateGroupAdmin(admin.ModelAdmin):

    readonly_fields = ('date_created', 'date_last_modified', )

admin.site.register(models.AssociateGroup, AssociateGroupAdmin)
