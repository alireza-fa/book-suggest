from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.book.serializers import BookListSerializer, BookReviewAddSerializer, BookReviewDetailSerializer
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
    permission_classes = (IsAuthenticated,)

    @extend_schema(tags=SCHEMA_TAGS)
    def get(self, request):
        pass


class BookReviewAddView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookReviewAddSerializer
    serializer_class_output = BookReviewDetailSerializer

    @extend_schema(tags=SCHEMA_TAGS)
    def post(self, request):
        # we also can get book_id from query parameter
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            return Response(
                status=status.HTTP_201_CREATED,
                data=self.serializer_class_output(instance=service.add_book_review(
                    user_id=request.user.id, **serializer.validated_data)).data
            )
        except Exception as err:
            return response_with_error(error=err)


class BookReviewUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookReviewAddSerializer

    @extend_schema(tags=SCHEMA_TAGS)
    def patch(self, request):
        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            service.update_book_review(user_id=request.user.id, **serializer.validated_data)
        except Exception as err:
            return response_with_error(error=err)

        return Response(status=status.HTTP_200_OK)


class BookReviewDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(tags=SCHEMA_TAGS)
    def delete(self, request):
        pass
