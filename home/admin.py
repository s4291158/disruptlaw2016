from django.contrib import admin

from home.models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    readonly_fields = ('time_stamp',)


admin.site.register(SignUp, SignUpAdmin)
