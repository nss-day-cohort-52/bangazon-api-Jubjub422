from django.urls import path
from .views import FavoriteStoreList

urlpatterns = [
    path('favorite_stores', FavoriteStoreList.as_view())
]
