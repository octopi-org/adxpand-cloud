"""amplifySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.decorators import api_view
from .views import index

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
#router.register(r'bentuition', views.Ben_TuitionViewSet)
router.register(r'bencampaign', views.BenCampaignViewSet)
router.register(r'benadgroup', views.BenAdGroupViewSet)
router.register(r'benmetrics', views.BenMetricsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('testview/', index, name='index')
    #path('show', views.showmodels, name='showmodels')
]
