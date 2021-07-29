from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    selected_passcard = get_object_or_404(Passcard, passcode=passcode)

    passcard_visits = Visit.objects.filter(passcard=selected_passcard)

    context = {
        "passcard": selected_passcard,
        "this_passcard_visits": passcard_visits
    }
    return render(request, 'passcard_info.html', context)
