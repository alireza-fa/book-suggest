from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.http_response import response_with_error
from user.serializers import UserAuthSerializer, UserInfoSerializer
from user.services import get_user_service


SCHEMA_TAGS = ("Users",)
service = get_user_service()


class UserLoginView(APIView):
    serializer_class = UserAuthSerializer
    serializer_class_output = UserInfoSerializer

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = service.login(**serializer.validated_data)
        except Exception as err:
            return response_with_error(error=err)

        return Response(status=status.HTTP_200_OK, data={
            "token": result["token"],
            "user": self.serializer_class_output(instance=result["user"]).data
        })


class UserRegisterView(APIView):
    serializer_class = UserAuthSerializer
    serializer_class_output = UserInfoSerializer

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = service.register(**serializer.validated_data)
        except Exception as err:
            return response_with_error(error=err)

        return Response(status=status.HTTP_201_CREATED, data={
            "token": result["token"],
            "user": self.serializer_class_output(instance=result["user"]).data
        })


class UserInfoView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserInfoSerializer

    @extend_schema(tags=SCHEMA_TAGS)
    def get(self, request):
        # TODO - implement me!!!
        pass
