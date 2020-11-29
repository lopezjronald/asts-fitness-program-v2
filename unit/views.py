from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Airman, Naughty, Profile, PhysicalTrainingLeader, UnitFitnessProgramManager
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .forms import SearchForm


# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.postgres.search import TrigramSimilarity


def airman_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('first_name', 'last_name', 'ssn', )
            search_query = SearchQuery(query)
            results = Airman.active.annotate(
                search=search_vector,
                ranking=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-ranking')
    return render(request,
                  'unit/airman/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})


# def airman_first_name_search(request):
#     form = SearchForm()
#     query = None
#     results = []
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = Airman.active.annotate(
#                 similarity=TrigramSimilarity('first_name', query),
#             ).filter(similarity__gt=0.1).order_by('-similarity')
#     return render(request,
#                   'unit/airman/search.html',
#                   {'form': form,
#                    'query': query,
#                    'results': results})

# def airman_list(request):
#     object_list = Airman.active.all()
#     paginator = Paginator(object_list, 10) # airmen in each page
#     page = request.GET.get('page')
#     try:
#         airmen = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         airmen = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         airmen = paginator.page(paginator.num_pages)
#     return render(request,
#                   'unit/airman/list.html',
#                   {'page': page,
#                    'airmen': airmen})

class AirmanListView(ListView):
    queryset = Airman.active.all()
    context_object_name = 'airmen'
    paginate_by = 10
    template_name = 'unit/airman/list.html'


def airman_detail(request, year, month, day, airman):
    airman = get_object_or_404(Airman,
                               airman_slug=airman,
                               active_status='active',
                               test_date__year=year,
                               test_date__month=month,
                               test_date__day=day)
    return render(request,
                  'unit/airman/detail.html',
                  {'airman': airman})


class NaughtyListView(ListView):
    model = Naughty
    template_name = 'unit/naughty/list.html'
    context_object_name = 'all_naughty_list'


class ProfileListView(ListView):
    model = Profile
    template_name = 'unit/profile/list.html'
    context_object_name = 'all_profile_list'


class PhysicalTrainingLeaderListView(ListView):
    model = PhysicalTrainingLeader
    template_name = 'unit/ptl/list.html'
    context_object_name = 'all_ptl_list'


class UnitFitnessProgramManagerListView(ListView):
    model = UnitFitnessProgramManager
    template_name = 'unit/ufpm/list.html'
    context_object_name = 'all_ufpm_list'
