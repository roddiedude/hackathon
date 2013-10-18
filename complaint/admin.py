from django.contrib import admin
from complaint.models import Complaint, Comments

admin.site.register(Complaint)
admin.site.register(Comments)