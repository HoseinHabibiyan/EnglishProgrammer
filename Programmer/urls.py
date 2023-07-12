from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls.static import static 
from django.conf import settings  
from django.contrib import admin
from .views import refrence_list ,register , login_view , refrence_detail , refrence_list , weekplan_list , weekplan_detail

urlpatterns = [
    path('', refrence_list, name='home'),
    path('register/', register, name='register'),
    path('accounts/login/', RedirectView.as_view(pattern_name='login', permanent=True)),
    path('login/',  login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('refrence_list/', refrence_list, name='refrence_list'),
    path('refrence_detail/<int:pk>/', refrence_detail, name='refrence_detail'),
    path('weekplan_list/', weekplan_list, name='weekplan_list'),
    path('weekplan_detail/<int:pk>/', weekplan_detail, name='weekplan_detail'),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header  =  "English Programmer administration Panel"  
admin.site.site_title  =  "English Programmer"
admin.site.index_title  =  "English Programmer"

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)