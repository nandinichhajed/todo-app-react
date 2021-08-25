from django.contrib import admin
from .models import Tractor,Tractor_Types,Tractor_Sub_Types_Activities
from store.models import (
    ProductImage,
    
)
admin.site.register(Tractor_Types)
admin.site.register(Tractor_Sub_Types_Activities)
admin.site.register(Tractor)


