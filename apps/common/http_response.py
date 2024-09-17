from rest_framework.response import Response

from apps.common.codes import ERROR_TRANSLATION, INTERNAL_SERVER_ERROR
from pkg.rich_error.error import error_code


def response_with_error(error: Exception) -> Response:
    code = error_code(error=error)
    return Response(status=code//100, data={"error": ERROR_TRANSLATION.get(code, INTERNAL_SERVER_ERROR)})
