from django.contrib import admin

from . import models


class EventAdmin(admin.ModelAdmin):
    
    list_display = ('title_en', 'date_from', 'date_until', )
    prepopulated_fields = {"slug": ("title_en",)}


class EventPartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'datetime_from', 'datetime_until', 
            'max_number_of_participants', 'is_bookable', )

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('one_line_description', )
    readonly_fields = ('price', )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'is_sold', 'price', 'number_of_items_available', )

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('one_line_description', )
    list_filter = ('paid_by', )
    
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('one_line_description', )
    
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventPart, EventPartAdmin)
admin.site.register(models.Registration, RegistrationAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Purchase, PurchaseAdmin)
admin.site.register(models.PurchaseItem, PurchaseItemAdmin)
