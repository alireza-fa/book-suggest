# API DOCS
SPECTACULAR_SETTINGS = {
    'TITLE': 'Book Api',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': True,
    # OTHER SETTINGS
    'PLUGINS': [
        'drf_spectacular.plugins.AuthPlugin',
    ],
    # 'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAdminUser'],
    # Auth with session only in docs without effect to api
    'SERVE_AUTHENTICATION': ["rest_framework.authentication.SessionAuthentication",
                             "rest_framework_simplejwt.authentication.JWTAuthentication"],
}
