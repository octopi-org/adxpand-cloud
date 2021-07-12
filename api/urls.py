from .views import index, AppGetView
from django.urls import include, path
from rest_framework import routers
import api.views as views

router = routers.DefaultRouter()
#router.register(r'bentuition', views.Ben_TuitionViewSet)
router.register(r'bencampaign', views.BenCampaignViewSet)
router.register(r'benadgroup', views.BenAdGroupViewSet)
router.register(r'benmetrics', views.BenMetricsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #the above line is how u get the login for drf
    path('GAlist/', views.GAlist, name='GAlist'),
    path('testview/', views.index, name='index'),
    path('appgetview/', AppGetView.as_view() , name='appgetview')
]