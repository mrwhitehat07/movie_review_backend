from django.urls import path
from celebs.views import CelebrityListView, CelebrityDetailView, RoleView, RoleDetailView, celebs_movies

urlpatterns = [
    path('celebs/', CelebrityListView.as_view(), name="celebs"),
    path('celebs/<int:pk>', CelebrityDetailView.as_view(), name="celebs"),
    path('celebs/<int:cid>/movies', celebs_movies, name="celebs"),
    path('role/', RoleView.as_view(), name="roles"),
    path('role/<int:pk>', RoleDetailView.as_view(), name="roles"),
]