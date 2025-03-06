from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.task_list, name="task_list"),
    path("add/", view=views.add_task, name="add_task"),
    path("edit/<int:pk>/", view=views.edit_task, name="edit_task"),
    path("delete/<int:pk>/", view=views.delete_task, name="delete_task"),
    path("complete/<int:pk>/", view=views.complete_task, name="complete_task"),
]
