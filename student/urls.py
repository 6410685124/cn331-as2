from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("<str:name>", views.class_detail, name="class_detail"),
    path("<int:student_id>/<str:name>/remove", views.remove_student_from_class, name="remove_student"),
    path("<int:student_id>/<str:name>/add", views.add_student_to_class, name="add_student"),
]