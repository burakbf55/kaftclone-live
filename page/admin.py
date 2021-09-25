from django.contrib import admin
from page.models import Carousel, Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status',
        'updated_at',
    )
    list_filter=('status',)
    list_editable=(
        'status',
        'title',
    )

class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
    )
    list_filter=('status',)
    
admin.site.register(Page,PageAdmin)
admin.site.register(Carousel,CarouselAdmin)