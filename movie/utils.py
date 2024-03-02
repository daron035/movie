

from .models import *

class DataMixin:
    
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        genre = Genre.objects.values('name').all()
        # last_mov = Movie.objects.values('title', 'poster').order_by('time_create')[:5]
        last_mov = Movie.objects.order_by('-time_create')[:5]
        
        context['cats'] = cats
        context['genre_left'] = genre
        context['last_mov'] = last_mov

        return context