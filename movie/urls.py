from django.urls import path, include

from .views import *

urlpatterns = [
    path('contact/', include('contact.urls')),
    path('', MovieHome.as_view(), name='index'),
    path('filter/', FilterMovie.as_view(), name='filter_movie'),
    path('search/', SearchMovie.as_view(), name='search'),
    path('movie/<slug:movie_url>/', ShowPost.as_view(), name='single'),
    path('staff/<str:slug>/', ShowStaff.as_view(), name='staff_single'),
    path('category/<slug:cat_url>', MovieCategory.as_view(), name='category'),
    # path('review/<int:pk>/', AddRewiew.as_view(), name='review'),
    path('review/<int:pk>/', AddReview.as_view(), name='review'),
    path('addmovie/', AddMovie.as_view(), name='addmovie'),
]