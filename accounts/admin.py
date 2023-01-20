from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import NewUser


fields = list(UserAdmin.fieldsets)
fields[1] = (
            'Personal Info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'degree',
                    'year',
                    'program'
                )
            }
    )
UserAdmin.fieldsets = tuple(fields)

class Customview(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','degree', 'year', 'program']

admin.site.register(NewUser,Customview)






# from .models import CustomUser

# class AccountInline(admin.StackedInline):
#     model = CustomUser
#     can_delete = False

# class CustomizedUserAdmin(UserAdmin):
    
#     def add_view(self, *args, **kwargs):
#         self.inlines= []
#         return super(CustomizedUserAdmin, self).add_view(*args, **kwargs)

#     def change_view(self, *args, **kwargs):
#         self.inlines= [AccountInline]
#         return super(CustomizedUserAdmin, self).change_view(*args, **kwargs)

# class Customview(admin.ModelAdmin):
#     list_display = ['user','degree', 'year', 'program']

# admin.site.unregister(User)
# admin.site.register(User, CustomizedUserAdmin)
# admin.site.register(CustomUser,Customview)