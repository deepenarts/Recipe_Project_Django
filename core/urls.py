
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="home"),
    path("recipes/", recipes, name="recipes"),
    path("delete_recipe/<id>/", delete_recipe, name= "delete_recipe"),
    path ("update_recipe/<id>/",update_recipe, name="update_recipe"),
    path("login/", login_page, name="login_page"),
    path("register/",register, name="register"),
    path ("logout/",logout_user, name="logout_user")
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()