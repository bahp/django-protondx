"""lacewing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# Rest API framework
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

# ----------------------------------
# Change basic admin template names
# ----------------------------------
# Change basic admin template names
admin.site.site_header = "ProtonDx administration"
admin.site.site_title = "ProtonDx | Administration"
admin.site.index_title = "ProtonDx | Administration"

urlpatterns = [
    # Add django admin
    path('admin/', admin.site.urls),

    # Add login/out views
    path('accounts/', include('django.contrib.auth.urls')),

    # Add diagnostics application
    path('diagnostics/', include('diagnostics.urls')),

    # Add dashboard application
    path('dashboard/', include('dashboard.urls')),

    # Add dataUpload application
    path('dataUpload/', include('dataUpload.urls')),

    #  ------------------------------------------
    # Adding full REST API
    # ------------------------------------------
    # .. note: In the scenario of big project it might be necessary to keep
    #          updating the API. As such, it might be useful to have also
    #          these API versions controlled.
    #           (READ MORE ABOUT THIS WHEN NEEDED)
    #
    #  re_path('api/(?P<version>(v1|v2))/', include('trials.urls')),
    #
    # API documentation
    # ----------------------
    # Add coreapi docs (requires coreapi)
    path('api/schema/coreapi/', include_docs_urls(title='EPiC IMPOC API')),
    # Add default schema
    path('api/schema/default/', get_schema_view(title='EPiC IMPOC API')),
    #  Add Swagger schema (requires swagger - not working)
    # path('api/schema/swagger/', get_swagger_view(title='EPiC IMPOC API')),
]
