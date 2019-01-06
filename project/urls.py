"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
#import rest_framework_swagger.urls
#from rest_framework_docs import urls as rest_api__urls

# schema_view = get_swagger_view(title='Описание API')

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls import static

schema_view = get_schema_view(
   openapi.Info(
      title="Описание API",
      default_version='v1',
      description="Описание API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)


class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        # renderers.CoreJSONRenderer,
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('rest_registration.api.urls')),
    path('api/', include('api.urls')),
    #path('swagger/', SwaggerSchemaView.as_view()),
    # path('swagger2(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('redocs/', include('redocs.urls')),
    #path('docs/', include('rest_framework_docs.urls')),
    #path('docs/', rest_api__urls.as_view()),
    #url(r'^docs/', include('rest_framework_docs.urls'))
    #path('docss/', include('rest_framework_docs.urls')),
]
#urlpatterns = (urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

admin.site.site_header = 'Администрирование Judge_App'
