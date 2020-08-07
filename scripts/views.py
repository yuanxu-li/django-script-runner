from django.shortcuts import render
from .scripts import run

# Create your views here.
def index(request):
    var_names = run.__code__.co_varnames
    context = {
        'var_names': var_names,
        'func_name': run.__code__.co_name
    }
    # Get all vars from the form if available
    var_values = [request.GET.get(var_name, '') for var_name in var_names]
    if all(var_values):
        result = run(*var_values)
        context['result'] = result
    return render(
        request=request,
        template_name='scripts/index.html',
        context=context,
    )
