from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Medicine
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search_medicines(request):
    """API endpoint to search for medicines"""
    if request.method == 'GET':
        search_term = request.GET.get('q', '').strip()
        
        if search_term:
            # Search in name, category, and notes fields
            medicines = Medicine.objects.filter(
                name__icontains=search_term
            ) | Medicine.objects.filter(
                category__icontains=search_term
            ) | Medicine.objects.filter(
                notes__icontains=search_term
            )
        else:
            medicines = Medicine.objects.none()
        
        # Convert to list of dictionaries
        medicines_data = []
        for medicine in medicines:
            medicines_data.append({
                'id': medicine.id,
                'name': medicine.name,
                'category': medicine.category,
                'dosage': medicine.dosage,
                'species_applicable': medicine.species_applicable,
                'notes': medicine.notes,
            })
        
        return JsonResponse({
            'medicines': medicines_data,
            'count': len(medicines_data)
        })
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)