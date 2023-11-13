
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

'''
def index(request):
    return HttpResponse("소금의 투두 리스트 만들기")
'''


def index(request):
    todos = Todo.objects.all()
    print("From DB:", todos)
    content= {'todos': todos }
    return render(request, "my_to_do_app/index.html", content)

def createTodo(request):
    user_input_str = request.POST['todoContent']

    new_todo= Todo(content =user_input_str)
    new_todo.save()

    return HttpResponseRedirect(reverse('index'))

    #return HttpResponse("메모한 건 여기에 쌓여요 : " + user_input_str)




