# from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
# from .models import Todo
# from django.http import HttpResponse, JsonResponse

from django.views.generic import TemplateView

class TodoView(TemplateView):
        template_name = 'todo/index.html'