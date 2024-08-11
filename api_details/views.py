from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import WellData

# used for getting details for a single api well 
def get_annual_data(request):
    well_id = request.GET.get('well')
    well_data = get_object_or_404(WellData, well_id=well_id)
    response_data = {
        "oil": well_data.oil,
        "gas": well_data.gas,
        "brine": well_data.brine,
    }
    return JsonResponse(response_data)

#used for getting details of all the well
def get_all_data(request):
    well_data = WellData.objects.values('well_id','oil','gas','brine')
    response_data = list(well_data)
    return JsonResponse(response_data, safe=False)