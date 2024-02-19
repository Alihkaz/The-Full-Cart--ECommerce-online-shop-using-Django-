

from django.contrib import admin
from .models import Products , Order


#customasing the admin panel :

admin.site.site_header="Chick-Clocks Shop"

admin.site.site_title="Chick-Clocks Shop"

admin.site.index_title="Manage Your Shop"


class ProductAdmin(admin.ModelAdmin):

    #modifying the action field :
    def change_category_to_default(self,request,queryset):
        queryset.update(category=default)

    search_fields=('title',) #adding a search field
    list_display=('title', 'price', 'discount_price', 'category',) #to change the appearance of the fields 
    actions=('change_category_to_default',)
    fields=('title','price','description',) #the fields to diplay when we click on a certain item 
    list_editable=('price',) #to let the price field editable ! 


admin.site.register(Products , ProductAdmin)
admin.site.register(Order)