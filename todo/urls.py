from django.urls import path
from .views import CreateTaskView, GetTaskView, ListTasksView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('create-task/', CreateTaskView.as_view(), name='create_task'),
    path('get-task/<int:pk>/', GetTaskView.as_view(), name='get_task'),
    path('list-tasks/<int:user_id>/', ListTasksView.as_view(), name='list_tasks'),
    path('update-task/', UpdateTaskView.as_view(), name='update_task'),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
]
