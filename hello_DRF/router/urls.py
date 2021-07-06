from .views import create_records, template_view
from django.conf import settings
from django.urls import path
from rest_framework import routers

app_name = 'router'

router = routers.SimpleRouter()
router.register(r'router', create_records)
router.register(r'template', template_view)
urlpatterns = router.urls

# urlpatterns = [
#     path('router/', create_records),
#     path('template/', template_view)
# ]
