from django.contrib import admin

# Register your models here.
from .models import *
	# Register your models here.

admin.site.register(Books) 
admin.site.register(Publisher) 
admin.site.register(Reader) 
admin.site.register(Staff)
admin.site.register(System)
