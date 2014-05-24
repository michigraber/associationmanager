from django.contrib import admin

from . import models


class EventAdmin(admin.ModelAdmin):
    
    list_display = ('title_en', 'date_from', 'date_until', )
    prepopulated_fields = {"slug": ("title_en",)}


class EventPartAdmin(admin.ModelAdmin):
    pass

class RegistrationAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    pass
    
class PurchaseAdmin(admin.ModelAdmin):
    pass
    
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ('one_line_description', )
    
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventPart, EventPartAdmin)
admin.site.register(models.Registration, RegistrationAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Purchase, PurchaseAdmin)
admin.site.register(models.PurchaseItem, PurchaseItemAdmin)
