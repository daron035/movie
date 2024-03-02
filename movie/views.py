from re import template
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Movie, Reviews
from .forms import *
from .utils import *
from .serializers import MovieSerializer


class MovieViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    

# Serializers




# Views

class MovieHome(DataMixin, ListView):
    model = Movie
    paginate_by = 9
    template_name = 'movie/movie_list.html'
    context_object_name = 'movies'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context() 
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Movie.objects.all()

class FilterMovie(MovieHome):
    
    def get_queryset(self):
        wewewe = self.request.GET.getlist('year[]')
        c = list(map(int, wewewe))
        b = self.request.GET.getlist('genre')
        
        qs = []
        if b and c:
            for i in c:
                try:
                    q = Movie.objects.get(Q(age__range=(i, i+10)) & Q(genre__name__in=b))
                    print(q)
                except:
                    continue
                qs.append(q)
        elif  b and not c:
            print(True)
            qs = Movie.objects.filter(genre__name__in=b)
        else:
            for i in c:
                try:
                    q = Movie.objects.get(age__range=(i, i+10))
                except:
                    continue
                qs.append(q)
        return qs
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.request.GET.getlist('year[]')
        b = self.request.GET.getlist('genre')
        context['age'] = ''.join([f'age={x}&' for x in c]) # for paginate.html
        context['genre'] = ''.join([f'genre={x}&' for x in b]) # for paginate.html
        return context
    
class SearchMovie(MovieHome):

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get('search'))
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.request.GET.getlist('search')
        context['q'] = ''.join(f'search={c}') # for paginate.html
        return context
    
class MovieCategory(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    slug_url_kwarg = 'cat_url'
    context_object_name = 'movies'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        context['cats'] = cats
        return context

    def get_queryset(self):
        return Movie.objects.filter(category__url=self.kwargs['cat_url'])
    
    
    
class ShowPost(DataMixin, DetailView):
    # form_class = AddReviewForm
    model = Movie
    template_name = 'movie/movie_single.html'
    slug_url_kwarg = 'movie_url'
    context_object_name = 'movie'

    def get_context_data(self, *, object_list=None, **kwargs): # возвращаем все посты из модели Women
        context = super().get_context_data(**kwargs)
        # context['star_form'] = RatingForm()
        context['form'] = AddReviewForm()
        return context
        
    def get_object(self):
        # if self.request.GET.get('search'):
        #     return Movie.objects.get(title=self.request.GET.get('search'))
        # else:
        #     return Movie.objects.get(url=self.kwargs['movie_url'])
        return Movie.objects.get(url=self.kwargs['movie_url'])
    
class ShowStaff(DetailView):
    model = Actor
    template_name = 'movie/staff_single.html'
    slug_field = 'name'
    context_object_name = 'staff'
    

# class AddRewiew(View):

#     def post(self, request, pk):
#         print(request.POST)
#         return reverse('index')

class AddReview(View):
    def post(self, request, pk):
        form = AddReviewForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            # form.movie_id = pk
            form.save()
        return redirect(movie.get_absolute_url())

class AddMovie(LoginRequiredMixin, DataMixin, CreateView):
    login_url = reverse_lazy('account_login')
    form_class = AddMovie
    template_name = 'movie/add.html'
    success_url = reverse_lazy('index')
    # raise_exception = True
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context() 
        context = dict(list(context.items()) + list(c_def.items()))
        return context