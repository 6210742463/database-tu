from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard", dashboard, name="dashboard"),
    path("create", create, name="create"),
    path("edit/<int:id>", edit, name="edit"),
    path("removeData/<int:id>", removeData, name="removeData"),
    path("title", title, name="title"),
    path("county", county, name="county"),
    path("doSomething", doSomething, name="doSomething"),
    path("faculty", faculty, name="faculty"),
]
