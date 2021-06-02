from .router import router
from django.urls import path, include

urlpatterns = [
    # api/movies/
    path('', include(router.urls))
]


"""
router: sets the las endpoint

in the urls (from metflix_remake the main) we got
'api' then include the api for movies letting an endpoint:
'api/movies/'

So it would be interesting to make the same to the other APIs (directors, actors...)

"""