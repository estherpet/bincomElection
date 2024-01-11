import MySQLdb._exceptions
from django.shortcuts import render, redirect

# Create your views here.
from .models import PollingUnit, AnnouncedPuResult, LGA, State, Ward
from django.db.models import Sum


def polling_unit_result(request, polling_unit_id):
    polling_unit = PollingUnit.objects.get(id=polling_unit_id)
    results = AnnouncedPuResult.objects.filter(polling_unit=polling_unit)
    return render(request, 'election_results/polling_unit_result.html',
                  {'polling_unit': polling_unit})


def lga_summed_results(request):
    lgas = LGA.objects.all()
    selected_lga = request.GET.get('lga', None)

    if selected_lga:
        polling_units = PollingUnit.objects.filter(ward__lga__id=selected_lga)
        results = AnnouncedPuResult.objects.filter(polling_unit__in=polling_units) \
            .values('party') \
            .annotate(total_score=Sum('score'))
        selected_lga_name = LGA.objects.get(id=selected_lga).name
    else:
        results = []
        selected_lga_name = None

    return render(request, 'election_results/lga_summed_results.html',
                  {'lgas': lgas, 'results': results, 'selected_lga': selected_lga,
                   'selected_lga_name': selected_lga_name})


def add_polling_unit_result(request):
    states = State.objects.all()

    if request.method == 'POST':
        state_id = request.POST.get('state')
        lga_id = request.POST.get('lga')
        ward_id = request.POST.get('ward')
        polling_unit_name = request.POST.get('polling_unit')
        party = request.POST.get('party')
        score = request.POST.get('score')

        try:
            state = State.objects.get(id=state_id)
            lga = LGA.objects.get(id=lga_id)
            ward = Ward.objects.get(id=ward_id)
            polling_unit, created = PollingUnit.objects.get_or_create(name=polling_unit_name, ward=ward)

            AnnouncedPuResult.objects.create(polling_unit=polling_unit, party=party, score=score)

            # Redirect to a success page or perform any other desired action
            return redirect('success_page')

        except MySQLdb._exceptions.IntegrityError:
            error_message = "Result for this party already exists for the selected polling unit."

    else:
        error_message = None

    return render(request, 'election_results/add_polling_unit_result.html',
                  {'states': states, 'error_message': error_message})
