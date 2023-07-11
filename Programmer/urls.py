from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls.static import static 
from django.conf import settings  
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.book_list, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/login/', RedirectView.as_view(pattern_name='login', permanent=True)),
    path('login/',  views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('book_list/', views.book_list, name='book_list'),
    path('book_detail/<int:pk>/', views.book_detail, name='book_detail'),
    # path('book_create/', views.book_create, name='book_create'),
    # path('book_update/<int:pk>/', views.book_update, name='book_update'),
    # path('book_delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('weekplan_list/', views.weekplan_list, name='weekplan_list'),
    # path('weekplan_create/', views.weekplan_create, name='weekplan_create'),
    path('weekplan_detail/<int:pk>/', views.weekplan_detail, name='weekplan_detail'),
    # path('weekplan_update/<int:pk>/', views.weekplan_update, name='weekplan_update'),
    # path('weekplan_delete/<int:pk>/', views.weekplan_delete, name='weekplan_delete'),
    # path('student_list/', views.student_list, name='student_list'),
    # path('student_create/', views.student_create, name='student_create'),
    # path('student_detail/<int:pk>/', views.student_detail, name='student_detail'),
    # path('student_update/<int:pk>/', views.student_update, name='student_update'),
    # path('student_delete/<int:pk>/', views.student_delete, name='student_delete'),
    # path('dailyprogram_create/', views.dailyprogram_create, name='dailyprogram_create'),
    # path('dailyprogram_create/<int:weekplan_id>/', views.dailyprogram_create, name='dailyprogram_create'),
    # path('dailyprogram_detail/<int:pk>/', views.dailyprogram_detail, name='dailyprogram_detail'),
    # path('dailyprogram_update/<int:weekplan_id>/<int:dailyprogram_id>/', views.dailyprogram_update, name='dailyprogram_update'),
    # path('dailyprogram_delete/<int:weekplan_id>/<int:dailyprogram_id>/', views.dailyprogram_delete, name='dailyprogram_delete'),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header  =  "English Programmer administration Panel"  
admin.site.site_title  =  "English Programmer"
admin.site.index_title  =  "English Programmer"

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)