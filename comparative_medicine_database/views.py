from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Medicine
from django.db.models import Q
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search_medicines(request):
    """API endpoint to search for medicines"""
    if request.method == 'GET':
        search_term = request.GET.get('q', '').strip()
        category = request.GET.get('category', '').strip()
        species = request.GET.get('species', '').strip()
        
        medicines = Medicine.objects.all()
        
        if search_term:
            medicines = medicines.filter(
                Q(name__icontains=search_term) |
                Q(category__icontains=search_term) |
                Q(notes__icontains=search_term) |
                Q(species_applicable__icontains=search_term)
            )
        
        if category:
            medicines = medicines.filter(category__icontains=category)
        
        if species:
            medicines = medicines.filter(species_applicable__icontains=species)
        
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

def get_all_medicines(request):
    """API endpoint to get all medicines for the dropdown"""
    if request.method == 'GET':
        medicines = Medicine.objects.all().order_by('name')
        
        medicines_data = []
        for medicine in medicines:
            medicines_data.append({
                'id': medicine.id,
                'name': medicine.name,
                'category': medicine.category,
                'dosage': medicine.dosage,
                'species_applicable': medicine.species_applicable,
                'notes': medicine.notes
            })
        
        return JsonResponse({'medicines': medicines_data})
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_medicine_detail(request, medicine_id):
    """API endpoint to get details of a specific medicine"""
    if request.method == 'GET':
        try:
            medicine = get_object_or_404(Medicine, id=medicine_id)
            
            medicine_data = {
                'id': medicine.id,
                'name': medicine.name,
                'category': medicine.category,
                'dosage': medicine.dosage,
                'species_applicable': medicine.species_applicable,
                'notes': medicine.notes
            }
            
            return JsonResponse(medicine_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=404)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)