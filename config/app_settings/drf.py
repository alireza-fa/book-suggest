REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.authentication.authenticate.JWTAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
