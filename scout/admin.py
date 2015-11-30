from django.contrib import admin

from .models import Province, District, Group, Ward

class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'district']}),
        ('Dates active', {'fields': ['start_date', 'end_date'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'district', 'is_active')
    search_fields = ['name']

admin.site.register(Ward)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Group, GroupAdmin)
