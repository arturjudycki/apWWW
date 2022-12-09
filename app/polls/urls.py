from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls')),
    path('osobas/perm_view/<int:pk>', views.person_view),
    path('osobas/', views.osoba_list),
    path('osobas/<int:pk>/', views.osoba_detail),
    path('osobas/update/<int:pk>/', views.osoba_update),
    path('osobas/delete/<int:pk>/', views.osoba_delete),
    path('osobas/add/', views.osoba_add),
    path('osobas/<str:letter>/', views.osoba_detail_name),
    # path('osobas/', views.OsobaList.as_view()),nieeeee
    # path('osobas/<int:pk>/', views.OsobaDetail.as_view()),
    # path('osobas/add/', views.OsobaAdd.as_view()),
    # path('osobas/<imie>/', views.OsobaDetailName.as_view()),
    # path('druzynas/', views.druzyna_list),
    # path('druzynas/<int:pk>/', views.druzyna_detail),
    # path('druzynas/add/', views.druzyna_add),
    # path('druzynas/<int:pk>/czlonkowie', views.druzyna_czlonkowie_detail),s
    path('druzynas/<int:pk>/', views.DruzynaDetail.as_view()),
]

