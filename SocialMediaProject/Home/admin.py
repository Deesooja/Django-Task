from django.contrib import admin

from Home.models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class MyCustomUserAdmin(BaseUserAdmin):
  # The fields to be used in displaying the User model.
  # These override the definitions on the base CustomUser
  # that reference specific fields on auth.User.
#   latitute=models.FloatField(null=True)
  list_display = ('id', 'is_admin','is_active','is_superuser','email', 'name', 'user_name', 'mobile' ,'term_conditions', 'profile_image' ,'address','pin_code', 'password','created_at','updated_at')
  list_filter = ('is_admin',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('name','mobile','address','pin_code','profile_image','term_conditions')}),
      ('Permissions', {'fields': ('is_admin','is_active')}),
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'name','mobile', 'term_conditions', 'password1', 'password2'),
      }),
  )
  search_fields = ('email',)
  ordering = ('id',)
  filter_horizontal = ()

admin.site.register(CustomUser, MyCustomUserAdmin)

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display =['id','user','friend']

@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display=['id','sender','resiver','action','accept','atempt','blocked','cancel_by_sender']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','user','image','text','for_all']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['id','user','post','action']
