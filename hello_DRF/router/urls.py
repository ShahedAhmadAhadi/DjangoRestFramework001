from .views import CreateRecords
from django.conf import settings
from django.urls import path
from rest_framework import routers

app_name = 'router'

router = routers.SimpleRouter()
router.register(r'router/', CreateRecords, basename='Emp')
# router.register(r'template', template_view)
urlpatterns = router.urls

# urlpatterns = [
#     path('router/', create_records),
#     path('template/', template_view)
# ]
