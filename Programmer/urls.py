from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls.static import static 
from django.conf import settings  
from django.contrib import admin
from .views import refrence_list ,register , login_view , refrence_detail , refrence_list , weekplan_list , weekplan_detail, refrence_series , refrence_seri_detail, home,language_list,language_detail , refrence_category ,category_detail ,refrence_skill_level,skill_level_detail , keyword_detail , refrence_keyword ,search_refrences

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('accounts/login/', RedirectView.as_view(pattern_name='login', permanent=True)),
    path('login/',  login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('refrence_list/', refrence_list, name='refrence_list'),
    path('search/', search_refrences, name='search_refrences'),
    path('refrence_series/', refrence_series, name='refrence_series'),
    path('language_list/', language_list, name='language_list'),
    path('refrence_category/', refrence_category, name='refrence_category'),
    path('refrence_skill_level/', refrence_skill_level, name='refrence_skill_level'),
    path('refrence_keyword/', refrence_keyword, name='refrence_keyword'),
    path('language_detail/<int:pk>/', language_detail, name='language_detail'),
    path('category_detail/<int:pk>/', category_detail, name='category_detail'),
    path('skill_level_detail/<int:pk>/', skill_level_detail, name='skill_level_detail'),
    path('keyword_detail/<int:pk>/', keyword_detail, name='keyword_detail'),
    path('refrence_detail/<slug:slug>/', refrence_detail, name='refrence_detail'),
    path('refrence_seri_detail/<slug:slug>/', refrence_seri_detail, name='refrence_seri_detail'),
    path('weekplan_list/', weekplan_list, name='weekplan_list'),
    path('weekplan_detail/<int:pk>/', weekplan_detail, name='weekplan_detail'),
    path('tinymce/', include('tinymce.urls')),
]

admin.site.site_header  =  "English Programmer administration Panel"  
admin.site.site_title  =  "English Programmer"
admin.site.index_title  =  "English Programmer"

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)