from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

from apps.book.serializers import BookListSerializer
from apps.book.services import get_book_service
from apps.common.http_response import response_with_error
from apps.common.pagination import PageNumberPagination

SCHEMA_TAGS = ("Books",)
service = get_book_service()


class BookListView(APIView):
    serializer_class = BookListSerializer
    pagination_class = PageNumberPagination

    @extend_schema(tags=SCHEMA_TAGS)
    def get(self, request):
        try:
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(
                queryset=service.search(search=request.GET), request=request)
            serializer = self.serializer_class(instance=paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as err:
            return response_with_error(error=err)


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
