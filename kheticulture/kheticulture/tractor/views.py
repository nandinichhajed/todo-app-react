from .models import Tractor
from django.shortcuts import get_object_or_404, render


def all_tractors(request):
    tractors = Tractor.objects.all()
    return render(request, 'tractor/home.html', {'tractors': tractors})
	
def add(request):
    tractor = Tractor(request)
    if request.POST.get('action') == 'post':
		
        response = JsonResponse({'success': 'Return something'})
        return response

# Create your views here.
