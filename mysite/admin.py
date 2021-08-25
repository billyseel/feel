from django.contrib import admin
from mysite import models
 
class PostAdmin(admin.ModelAdmin):
    list_display=('nickname', 'message', 'enabled', 'pub_time')
    ordering=('-pub_time',)#倒著數，這樣才不會54321
admin.site.register(models.Mood)
admin.site.register(models.Post, PostAdmin)