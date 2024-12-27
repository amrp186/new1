from django.contrib import admin
from .models import UserProfile
from .models import Appointment
from .models import Shift
from .models import Event

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Appointment)
admin.site.register(Shift)
admin.site.register(Event)
