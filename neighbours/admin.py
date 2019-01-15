from django.contrib import admin
from .models import Neighborhood,Occupants,Business

# Site registration 
admin.site.register(Neighborhood)
admin.site.register(Occupants)
admin.site.register(Business)
