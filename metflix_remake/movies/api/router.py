from rest_framework.routers import DefaultRouter
from .views import MovieApiView

router = DefaultRouter()

# As this api will be small this is not needed but it makes more
# easy to read and work with django
router.register(
    prefix='movies', basename='movies', viewset=MovieApiView
)
