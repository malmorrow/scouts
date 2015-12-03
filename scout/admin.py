from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Branch, District, Doctor, Group, Parent, Province, Ward

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'is_active')
    search_fields = ['name']

admin.site.register(Branch)
admin.site.register(District)
admin.site.register(Doctor)
admin.site.register(Group, GroupAdmin)
admin.site.register(Parent)
admin.site.register(Province)
admin.site.register(Ward)

class ParentInline(admin.StackedInline):
	model = Parent
	can_delete = False
	verbose_plural_name = 'parent'

class WardInline(admin.StackedInline):
	model = Ward
	can_delete = False
	verbose_plural_name = 'ward'
'''
class UserAdmin(UserAdmin):
	inlines = (ParentInline, WardInline, )
'''
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
