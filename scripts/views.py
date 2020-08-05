from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .scripts import num_vars, add_func

# Create your views here.
def index(request):
    context = {'num_vars': num_vars}
    # Get all vars from the form if available
    vars = [request.GET.get('var_' + str(i), '') for i in range(num_vars)]
    if all(vars):
        result = add_func(*vars)
        context['result'] = result
    return render(
        request=request,
        template_name='scripts/index.html',
        context=context,
    )
