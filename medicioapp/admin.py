from django.contrib import admin
from medicioapp.models import Product
from medicioapp.models import Branch
from medicioapp.models import Contact
from medicioapp.models import Appointment
from medicioapp.models import Member

# Register your models here.
admin.site.register(Product)
admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(Member)