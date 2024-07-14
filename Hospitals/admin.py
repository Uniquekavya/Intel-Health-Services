# Register your models here.
from django.contrib import admin
from.models import Hospital
from .models import Feedback

class Hospital_admin(admin.ModelAdmin):
    pass

admin.site.register(Hospital, Hospital_admin)


admin.site.register(Feedback)


