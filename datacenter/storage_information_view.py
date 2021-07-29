from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    context = {
        "non_closed_visits": Visit.objects.filter(leaved_at__isnull=True)
    }
    return render(request, 'storage_information.html', context)
