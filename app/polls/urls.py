from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('osobas/', views.osoba_list),
    # path('osobas/<int:pk>/', views.osoba_detail),
    # path('osobas/add/', views.osoba_add),
    # path('osobas/<imie>/', views.osoba_detail_name),
    path('osobas/', views.OsobaList.as_view()),
    path('osobas/<int:pk>/', views.OsobaDetail.as_view()),
    path('osobas/add/', views.OsobaAdd.as_view()),
    path('osobas/<imie>/', views.OsobaDetailName.as_view()),
    path('druzynas/', views.druzyna_list),
    path('druzynas/<int:pk>/', views.druzyna_detail),
    path('druzynas/add/', views.druzyna_add),
]