from rest_framework.response import Response
from rest_framework import status
from service_objects.services import Service

from career.commom.constant import MESSAGE, RECORD_CREATE_SUCCESSFULLY, YOU_HAVE_ALREADY_APPLIED_FOR_THIS_POSITION
from portal.models import JobDetails, ClientDetails


class JobDescriptionService(Service):
    def process(self):
        category = self.data["category"]
        responsibilities = self.data["responsibilities"]
        description = self.data['description']
        requirements = self.data["requirements"]
        obj = JobDetails.objects.create(category=category, responsibilities=responsibilities,
                                        requirements=requirements, description=description)
        return Response(
            {MESSAGE: RECORD_CREATE_SUCCESSFULLY, "job_id": obj.id}, status=status.HTTP_201_CREATED
        )


class ClientDescriptionService(Service):
    def process(self):
        job_id = self.data['job_id']
        job_obj = JobDetails.objects.get(id=job_id)
        first_name = self.data['first_name']
        last_name = self.data['last_name']
        email = self.data['email']
        phone_number = self.data['phone_number']
        address = self.data['address']
        experience = self.data['experience']
        city = self.data['city']
        state = self.data['state']
        pin_code = self.data['pin_code']
        upload_file = self.data['upload_file']
        obj = JobDetails.objects.filter(client_details__email=email)
        if obj.exists():
            return Response({MESSAGE: YOU_HAVE_ALREADY_APPLIED_FOR_THIS_POSITION},
                            status=status.HTTP_400_BAD_REQUEST)
        client_obj = ClientDetails.objects.create(first_name=first_name, last_name=last_name, email=email,
                                                  phone_number=phone_number,
                                                  address=address, experience=experience, city=city, state=state,
                                                  pin_code=pin_code, upload_file=upload_file)

        job_obj.client_details.add(client_obj)
        return Response(
            {MESSAGE: RECORD_CREATE_SUCCESSFULLY}, status=status.HTTP_201_CREATED
        )
