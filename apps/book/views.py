from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

SCHEMA_TAGS = ("Books",)


class BookListView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def get(self, request):
        pass


class BookSuggestView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def get(self, request):
        pass


class BookReviewAddView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        pass


class BookReviewUpdateView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def patch(self, request):
        pass


class BookReviewDeleteView(APIView):

    @extend_schema(tags=SCHEMA_TAGS)
    def delete(self, request):
        pass
