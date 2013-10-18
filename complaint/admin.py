from django.contrib import admin
from complaint.models import Complaint,Comments
from complaint.models import Following

admin.site.register(Complaint)
admin.site.register(Following)
admin.site.register(Comments)

