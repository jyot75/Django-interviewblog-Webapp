from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
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



from .models import Profile

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
admin.site.register(Profile,ContactAdmin)