from django.urls import path
from .views import FavoriteStoreList, IncompleteOrderList

urlpatterns = [
    path('favorite_stores', FavoriteStoreList.as_view()),
    path('incomplete_orders', IncompleteOrderList.as_view())
]
