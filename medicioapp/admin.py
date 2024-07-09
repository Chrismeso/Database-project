from django.contrib import admin
from medicioapp.models import Product
from medicioapp.models import Branch
from medicioapp.models import Contact

# Register your models here.
admin.site.register(Product)
admin.site.register(Branch)
admin.site.register(Contact)