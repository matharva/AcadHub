from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'login_app'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('editprofile/', views.profile, name="profile"),
	path('profile/<str:name>', views.profilepage, name="profilepage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)