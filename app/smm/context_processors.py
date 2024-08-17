# app/smm/context_processors.py

def is_manager(request):
    return {
        'is_manager': request.user.groups.filter(name='manager').exists() if request.user.is_authenticated else False
    }
