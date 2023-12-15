
from django.urls import path
from . import views

urlpatterns = [

    path('',views.add,name='add'),
    path('opening',views.opening,name='opening'),
    path('restroomcleaning', views.restroomcleaning, name='restroomcleaning'),
    path('transition', views.transition, name='transition'),
    path('closing', views.closing, name='closing'),
]
