from django.urls import path,include
import loaner_list.views
from django.http import HttpResponse,JsonResponse
from .views import add_loaner,search_loaner,Loaner_list,Loaner_update,reg
def index2(request):
    return JsonResponse({'user':'Json'})

urlpatterns = [
    path('list',loaner_list.views.get_index_page),
    path('index2/',index2),
    path('add_loaner/',add_loaner),
    path('search_loaner/',search_loaner),
    path('fbv/list/',Loaner_list),
    path('fbv/detail/<int:pk>/', Loaner_update),
    path('reg/',reg)
]