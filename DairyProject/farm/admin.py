from django.contrib import admin
from .models import CustomUser
from .models import Farmer , Society, IFSCcode


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Farmer)
admin.site.register(Society)
admin.site.register(IFSCcode)
