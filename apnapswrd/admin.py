from django.contrib import admin
from .models import contactus, newentry

admin.site.site_header = "Pswrd Mngr Admin"
admin.site.site_title = "Pswrd Mngr"

# Register your models here.
admin.site.register(contactus)
admin.site.register(newentry)