from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

SCHEMA_TAGS = ("Auth",)


class TokenVerifyView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        pass


class TokenRefreshView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        pass


class TokenBanView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        pass
