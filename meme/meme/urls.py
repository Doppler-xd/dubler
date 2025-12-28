from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Маршруты приложения memes
    path('', include('memes.urls')),

    # Стандартные маршруты авторизации Django
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True
    ), name='login'),

    path('memes/', include('memes.urls')),

    path('accounts/logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ), name='logout'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)