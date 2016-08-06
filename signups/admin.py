from django.contrib import admin

from signups.models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    readonly_fields = ('time_stamp',)


admin.site.register(SignUp, SignUpAdmin)
