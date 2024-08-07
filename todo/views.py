from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Task
import json

@method_decorator(csrf_exempt, name='dispatch')
class CreateTaskView(View):
    def put(self, request):
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            user_id=data.get('user_id')
        )
        return JsonResponse({'task_id': task.id}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class GetTaskView(DetailView):
    model = Task
    def get(self, request, *args, **kwargs):
        task = self.get_object()
        return JsonResponse({
            'task_id': task.id,
            'title': task.title,
            'description': task.description,
            'user_id': task.user_id,
            'created_at': task.created_at,
            'updated_at': task.updated_at
        })

@method_decorator(csrf_exempt, name='dispatch')
class ListTasksView(ListView):
    model = Task

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        tasks = Task.objects.filter(user_id=user_id)
        tasks_list = list(tasks.values())
        return JsonResponse(tasks_list, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateTaskView(View):
    def put(self, request):
        data = json.loads(request.body)
        task_id = data.get('task_id')
        task = Task.objects.get(id=task_id)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.save()
        return JsonResponse({'task_id': task.id})

@method_decorator(csrf_exempt, name='dispatch')
class DeleteTaskView(View):
    def delete(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        if not task:
            return JsonResponse({'error': 'Task not found'}, status=404)
        task.delete()
        return JsonResponse({'message': 'Task deleted'}, status=204)
        