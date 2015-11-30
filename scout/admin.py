from django.contrib import admin

from .models import Branch, Province, District, Group, Ward

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'is_active')
    search_fields = ['name']

admin.site.register(Branch)
admin.site.register(Ward)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Group, GroupAdmin)
