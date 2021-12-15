from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .models import Category, UserProfile, Projects, Rating
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", views.index, name="index"),

    path("projects/<int:id>", views.projects, name="projects"),
    path('submit-project/', views.submit_project,name="submit-project"),
    
    path("accounts/profile/", views.profile_view, name="profile"),

    path('api/projects/',views.ProjectList.as_view()),
    path('api/profiles/',views.UserProfileList.as_view()),
    path('api/categories/',views.CategoryList.as_view()),
    

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
