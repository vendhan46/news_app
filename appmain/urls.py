from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('demo', views.news_category, name='news_home'),
    path('home1',views.home1),
    path('',views.login,      name='login'),
    path('register/',     views.register,   name='register'),
    path('homepage',views.home, name='homepage'),
    path('news/<str:category>/', views.home, name='home'),
    path('gnews/<str:gcountry>/', views.home, name='gnews_news'),
    path('search',views.search,name='search'),
    path('profile',views.profile, name='profile'),
    path("update/<int:id>", views.update_profile, name="update_profile"),
    path('opinion/',views.opinion, name="opinion"),
    path('video/',views.videos, name="video"),
    path('bookmark/',views.bookmarks,name="bookmark"),
    path('subscribe',views.subscribe,name='subscribe')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)