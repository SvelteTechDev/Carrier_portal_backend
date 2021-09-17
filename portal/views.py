from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from career.commom.constant import ERROR, JOB_DOES_NOT_EXISTS
from portal.models import JobDetails, CategoryList
from portal.serializers import JobDescriptionSerializer, ClientDescriptionSerializer, categoryListSerializer, \
    DetailJobDescriptionSerializer, GetJobDescriptionSerializer
from portal.services import JobDescriptionService, ClientDescriptionService


class JobDescriptionListView(APIView):
    @staticmethod
    def post(request):
        serializer = JobDescriptionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return JobDescriptionService.execute(serializer.validated_data)

    @staticmethod
    def get(_):
        category = JobDetails.objects.all()
        return Response(DetailJobDescriptionSerializer(category, many=True).data)


class ClientDescriptionListView(APIView):
    @staticmethod
    def post(request):
        serializer = ClientDescriptionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return ClientDescriptionService.execute(serializer.validated_data)


class CategoryListDetailView(APIView):
    @staticmethod
    def get(_):
        category = CategoryList.objects.all()
        return Response(categoryListSerializer(category, many=True).data)


class JobDescriptionDetailView(APIView):
    @staticmethod
    def get(_, category_id):
        try:
            obj = JobDetails.objects.filter(category__id=category_id)
            return Response(GetJobDescriptionSerializer(obj, many=True).data, status=status.HTTP_200_OK)
        except JobDetails.DoesNotExist:
            return Response(
                {ERROR: [JOB_DOES_NOT_EXISTS.format(category_id)]},
                status=status.HTTP_404_NOT_FOUND,
            )


class JobDetailDescriptionDetailView(APIView):
    @staticmethod
    def get(_, job_id):
        try:
            obj = JobDetails.objects.get(id=job_id)
            return Response(DetailJobDescriptionSerializer(obj).data, status=status.HTTP_200_OK)
        except JobDetails.DoesNotExist:
            return Response(
                {ERROR: [JOB_DOES_NOT_EXISTS.format(job_id)]},
                status=status.HTTP_404_NOT_FOUND,
            )