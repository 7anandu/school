from  django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('button/',views.button,name='button'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('save/',views.Save,name='save'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),  # AJAX
]