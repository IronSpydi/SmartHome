from datetime import datetime
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def registration(request):
    if request.method == 'GET':
        users = User.objects.all()
        # control_system_registration = ControlSystemRegistration.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)

    if request.method == 'POST':
        # print(request.data["serial_no"])
        register = ControlSystemRegistration.objects.get(
            serial_no=request.data["serial_no"])
        # user = User.objects.all()
        exist_user = User.objects.get(email=request.data["email"])
        if exist_user or register.user_id is not None:
                # return Response({"message": "on this serial no and email another account is already registered"}, status=status.HTTP_409_CONFLICT)
            return Response({"message": "on this email or serial number another account is already registered"}, status=status.HTTP_409_CONFLICT)
        else:
            # serializer = UserSerializer(data={"name":request.data["name"],"email":request.data["email"],"phone_number":request.data["phone_number"]})
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.all()
                exist_user = user.get(email=request.data["email"])
                # user = User.objects.get(email=request.data["email"])
                register_datetime = str(datetime.strptime(
                    datetime.now, "%d/%m/%y %H:%M:%S.%f"))
                # ControlSystemRegistration.objects.filter(pk=request.data['serial_no']).update(user_id=user.id, registered_at=register_datetime)
                # exist_user = user.filter(email=request.data["email"])
                serialNo = ControlSystemRegistration.objects.get(
                    pk=request.data['serial_no'])
                serializer = ControlSystemRegistrationSerializer(serialNo, data={
                                                                 "user_id": exist_user.id, "registered_at": register_datetime}, partial=True)  # set partial=True to update a data partially
                if serializer.is_valid():
                    serializer.save()
                return Response({"message": "registered successfully"}, status=status.HTTP_201_CREATED)
