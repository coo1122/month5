from django.urls import path
from films import views
from utils.constans import LIST_CREATE, RETRIEVE_UPDATE_DESTROY

urlpatterns = [
    path('', views.film_list_create_api_view),
    path('<int:id>/', views.film_detail_api_view),
    path('directors/', views.DirectorListAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('genres/', views.GenreViewSet.as_view(LIST_CREATE)),
    path('genres/<int:id>/', views.GenreViewSet.as_view(RETRIEVE_UPDATE_DESTROY))
]