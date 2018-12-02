from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from maths.models import Math

# Create your views here.

def calculate(operation, arg_a, arg_b):...


def math_operations(request, operation, arg_a, arg_b):
    result = None
    Math.objects.create(operation=operation, arg_a, arg_b=arg_b)
    if operation == "add":
        result = arg_a + arg_b
    elif operation == "sub":
        result = arg_a - arg_b

    return HttpResponse(result)

def math_list(request):
    object = Math.objects.all()
    return render(
        request=req,
        template_name="math_list.html",
        context={"maths: objects"}
                  )

    out = ""
    for o in objects:
        out += f"{o.operation}: {o.arg_a} {o.arg_b} <br>"

    return HttpResponse(out)

def math_details(request, id):
    m = Math.objects.get(pk=id)

    out = f"""
Operacja: {m.operation}<br>
arg 1: {m.arg_a}<br>
arg 1: {m.arg_b}<br>
---------------------<br>
wynik:{calculate(m.operation, m.arg_a, m.arg_b)}<br>"""

    return HttpResponse(out)