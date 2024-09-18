from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import TokenSerializer
from authentication.services import get_authentication_service
from common.http_response import response_with_error

SCHEMA_TAGS = ("Auth",)
service = get_authentication_service()


class TokenVerifyView(APIView):
    serializer_class = TokenSerializer

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service.validate_token(token_str=serializer.validated_data["token"])
        except Exception as err:
            return response_with_error(error=err)

        return Response(status=status.HTTP_200_OK)


class TokenRefreshView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        pass


class TokenBanView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        pass
