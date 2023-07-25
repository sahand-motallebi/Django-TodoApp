from django.urls import path
from .views import (
    TaskList,
    TaskCreate,
    TaskComplete,
    TaskUpdate,
)
from . import views


urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
    path("create/", TaskCreate.as_view(), name="create_task"),
    path("update/<int:pk>/", TaskUpdate.as_view(), name="update_task"),
    path("complete/<int:pk>/", TaskComplete.as_view(), name="complete_task"),
    path("delete/<str:pk>/", views.deleteTask, name="delete_task"),
]
