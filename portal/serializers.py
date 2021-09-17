from rest_framework import serializers

from portal.models import JobDetails, ClientDetails, CategoryList


class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetails
        fields = (
            "category", "responsibilities", "requirements", 'description'
        )


class ClientDescriptionSerializer(serializers.ModelSerializer):
    job_id = serializers.IntegerField()

    class Meta:
        model = ClientDetails
        fields = (
            "first_name", "last_name", "email", "phone_number", "experience", "address", "city", "state", "pin_code",
            "job_id", "upload_file")


class categoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryList
        fields = ('id', "category",)


class GetJobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetails
        fields = (
            "id", "title", "description")


class DetailJobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetails
        fields = (
            'id', "title", "responsibilities", "requirements", 'description'
        )

