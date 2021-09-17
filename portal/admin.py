from django.contrib import admin
# Register your models here.
from portal.models import JobDetails, CategoryList
from django_summernote.admin import SummernoteModelAdmin


# creating admin class
class JobDetailsadmin(SummernoteModelAdmin):
    summernote_fields = ('responsibilities', "requirements")


admin.site.register(JobDetails, JobDetailsadmin)
admin.site.register(CategoryList)
