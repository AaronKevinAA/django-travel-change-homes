from django.contrib import admin

# Register your models here.
from XXX.models import LoginUser, UserInfo, HomeImage, UserPublish, UserHome, RealName,BannerImage


class LoginUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'pwd')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'account', 'head_img', 'credit')


class RealNameAdmin(admin.ModelAdmin):
    list_display = ('rnid', 'email', 'name', 'age', 'sex', 'phone', 'idnumber', 'idfront', 'idbehind', 'date', 'status')


class UserHomeAdmin(admin.ModelAdmin):
    list_display = ('hid', 'email', 'name', 'location', 'area', 'type', 'prove', 'prove_date', 'status')


class UserPublishAdmin(admin.ModelAdmin):
    list_display = (
    'pid', 'email', 'home_name', 'title', 'price', 'start_date', 'end_date', 'situation_desc', 'facilities', 'role',
    'date', 'status')


class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('pid', 'image_id', 'image')


class BannerImgAdmin(admin.ModelAdmin):
    list_display = ('bid','image','text_desc','status')

admin.site.register(LoginUser, LoginUserAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(RealName, RealNameAdmin)
admin.site.register(UserHome, UserHomeAdmin)
admin.site.register(UserPublish, UserPublishAdmin)
admin.site.register(HomeImage,HomeImageAdmin)
admin.site.register(BannerImage,BannerImgAdmin)