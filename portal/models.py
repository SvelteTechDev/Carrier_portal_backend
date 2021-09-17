from django.db import models

# Create your models here.


class ClientDetails(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254,  blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    experience = models.DecimalField(max_digits=19,decimal_places=2,default=0.0)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pin_code = models.IntegerField(blank=True, null=True)
    upload_file = models.FileField(upload_to='portal/client_cv/')


class CategoryList(models.Model):
    category = models.CharField(max_length=255)


class JobDetails(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryList, on_delete=models.CASCADE)
    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    client_details = models.ManyToManyField(ClientDetails, related_name='job_client_detail',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
