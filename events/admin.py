from django.contrib import admin

from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'date_from', 'date_until', )
    prepopulated_fields = {"slug": ("title_en",)}
    readonly_fields = ('date_created', 'date_last_modified', )

class EventPartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'datetime_from', 'datetime_until', 
            'max_no_participants', 'no_eventparts_assigned', 'is_bookable', 'still_available', )
    readonly_fields = ('date_created', 'date_last_modified', )

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('one_line_description', 'get_payment_status_display', )
    readonly_fields = ('price', 'date_created', 'date_last_modified', )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'is_sold', 'price', 'no_articles_available', )
    readonly_fields = ('date_created', 'date_last_modified', )

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('one_line_description', 'associate', 'balance_due', 'get_payment_status_display',)
    list_filter = ('payment_status', )
    readonly_fields = ('date_created', 'date_last_modified', )
    
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('one_line_description', 'get_payment_status_display', ) 
    readonly_fields = ('date_created',
                    'date_last_modified', )

    
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventPart, EventPartAdmin)
admin.site.register(models.Registration, RegistrationAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Purchase, PurchaseAdmin)
admin.site.register(models.PurchaseItem, PurchaseItemAdmin)
