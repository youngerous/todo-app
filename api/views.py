from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.generic import DeleteView, ListView
from django.views.generic.edit import BaseCreateView, BaseDeleteView
from django.views.generic.list import BaseListView
from django.forms import model_to_dict


import json
from todolists.models import Todo

@method_decorator(ensure_csrf_cookie, name='dispatch')
class ApiTodoListView(BaseListView):
    model = Todo

    def render_to_response(self, context, **response_kwargs):
        todolists = list(context['object_list'].values())
        return JsonResponse(data=todolists, safe=False)


class ApiTodoDeleteView(BaseDeleteView):
    model = Todo

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)

class ApiTodoCreateView(BaseCreateView):
    model = Todo
    fields = '__all__'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['data'] = json.loads(self.request.body)
        return kwargs

    def form_valid(self, form):
        print("form_valid()", form)
        self.object = form.save()
        newTodo = model_to_dict(self.object)
        print(f"newTodo: {newTodo}")
        return JsonResponse(data=newTodo, status=201)

    def form_invalid(self, form):
        print("form_invalid()", form)
        print("form_invalid()", self.request.POST)
        print("form_invalid()", self.request.body.decode('utf8'))
        return JsonResponse(data=form.errors, status=400)
