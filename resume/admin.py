from django.contrib import admin

# Register your models here.

from .models import User,Education,Certification,Workexperience

admin.site.register(User)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Workexperience)
