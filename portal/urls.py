from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from portal.views import JobDescriptionListView, ClientDescriptionListView, CategoryListDetailView, \
    JobDescriptionDetailView, JobDetailDescriptionDetailView

urlpatterns = [
    path('jobDescription/', JobDescriptionListView.as_view(), name="job_details"),
    path('clientDescription/', ClientDescriptionListView.as_view(), name="client_details"),
    path('categoryList/', CategoryListDetailView.as_view(), name="list_category"),
    path('jobDetail/<int:category_id>/', JobDescriptionDetailView.as_view(), name='job_detail_list'),
    path('jobDetailDesc/<int:job_id>/', JobDetailDescriptionDetailView.as_view(), name='job_detail_description')
]