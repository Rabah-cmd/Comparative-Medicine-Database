from django.core.management.base import BaseCommand
from comparative_medicine_database.models import Medicine


class Command(BaseCommand):
    help = 'Populate the database with human medicines data'

    def handle(self, *args, **options):
        # Clear existing data
        Medicine.objects.all().delete()
        
        # Human medicines data
        medicines_data = [
            {
                'name': 'Ibuprofen',
                'category': 'Pain Reliever/Anti-inflammatory',
                'dosage': '200mg tablets',
                'species_applicable': 'Humans',
                'notes': 'NSAIDs for pain, fever, and inflammation. Take with food to reduce stomach irritation.'
            },
            {
                'name': 'Amoxicillin',
                'category': 'Antibiotic',
                'dosage': '500mg capsules',
                'species_applicable': 'Humans',
                'notes': 'Penicillin-type antibiotic for bacterial infections. Complete full course even if feeling better.'
            },
            {
                'name': 'Metformin',
                'category': 'Diabetes Medication',
                'dosage': '500mg tablets',
                'species_applicable': 'Humans',
                'notes': 'First-line treatment for type 2 diabetes. Helps control blood sugar levels.'
            },
            {
                'name': 'Lisinopril',
                'category': 'ACE Inhibitor',
                'dosage': '10mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Blood pressure medication. Also used for heart failure and kidney protection.'
            },
            {
                'name': 'Atorvastatin',
                'category': 'Statin',
                'dosage': '20mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Cholesterol-lowering medication. Take in the evening for best effectiveness.'
            },
            {
                'name': 'Omeprazole',
                'category': 'Proton Pump Inhibitor',
                'dosage': '20mg capsules',
                'species_applicable': 'Humans',
                'notes': 'Reduces stomach acid production. Used for GERD, ulcers, and acid reflux.'
            },
            {
                'name': 'Aspirin',
                'category': 'Antiplatelet/Pain Reliever',
                'dosage': '81mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Low-dose aspirin for cardiovascular protection. Also used for pain and fever.'
            },
            {
                'name': 'Acetaminophen',
                'category': 'Pain Reliever/Fever Reducer',
                'dosage': '500mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Safe for most people. Avoid exceeding 3000mg per day to prevent liver damage.'
            },
            {
                'name': 'Ciprofloxacin',
                'category': 'Fluoroquinolone Antibiotic',
                'dosage': '250mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Broad-spectrum antibiotic. Avoid dairy products and antacids during treatment.'
            },
            {
                'name': 'Prednisone',
                'category': 'Corticosteroid',
                'dosage': '5mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Anti-inflammatory steroid. Taper dose gradually when discontinuing.'
            },
            {
                'name': 'Levothyroxine',
                'category': 'Thyroid Hormone',
                'dosage': '50mcg tablets',
                'species_applicable': 'Humans',
                'notes': 'Thyroid hormone replacement. Take on empty stomach, 30-60 minutes before breakfast.'
            },
            {
                'name': 'Gabapentin',
                'category': 'Anticonvulsant/Neuropathic Pain',
                'dosage': '300mg capsules',
                'species_applicable': 'Humans',
                'notes': 'Used for nerve pain and seizures. May cause drowsiness, especially when starting.'
            },
            {
                'name': 'Sertraline',
                'category': 'SSRI Antidepressant',
                'dosage': '50mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Selective serotonin reuptake inhibitor for depression and anxiety disorders.'
            },
            {
                'name': 'Warfarin',
                'category': 'Anticoagulant',
                'dosage': '5mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Blood thinner. Requires regular INR monitoring and dietary vitamin K consistency.'
            },
            {
                'name': 'Hydrochlorothiazide',
                'category': 'Diuretic',
                'dosage': '25mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Water pill for high blood pressure and fluid retention. Monitor potassium levels.'
            },
            {
                'name': 'Furosemide',
                'category': 'Loop Diuretic',
                'dosage': '40mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Powerful diuretic for heart failure and edema. Monitor electrolytes closely.'
            },
            {
                'name': 'Insulin Glargine',
                'category': 'Long-acting Insulin',
                'dosage': '100 units/mL injection',
                'species_applicable': 'Humans',
                'notes': 'Basal insulin for diabetes management. Inject once daily at the same time.'
            },
            {
                'name': 'Amlodipine',
                'category': 'Calcium Channel Blocker',
                'dosage': '5mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Blood pressure medication. May cause ankle swelling in some patients.'
            },
            {
                'name': 'Albuterol',
                'category': 'Bronchodilator',
                'dosage': '90mcg inhaler',
                'species_applicable': 'Humans',
                'notes': 'Rescue inhaler for asthma and COPD. Shake well before each use.'
            },
            {
                'name': 'Losartan',
                'category': 'ARB (Angiotensin Receptor Blocker)',
                'dosage': '50mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Blood pressure medication. Alternative to ACE inhibitors for those with cough.'
            },
            {
                'name': 'Pantoprazole',
                'category': 'Proton Pump Inhibitor',
                'dosage': '40mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Acid reducer for GERD and peptic ulcers. Take before meals for best effect.'
            },
            {
                'name': 'Clopidogrel',
                'category': 'Antiplatelet',
                'dosage': '75mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Blood thinner to prevent blood clots. Used after heart attacks or strokes.'
            },
            {
                'name': 'Tramadol',
                'category': 'Opioid Analgesic',
                'dosage': '50mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Pain medication for moderate to severe pain. Risk of dependence and seizures.'
            },
            {
                'name': 'Montelukast',
                'category': 'Leukotriene Modifier',
                'dosage': '10mg tablets',
                'species_applicable': 'Humans',
                'notes': 'Asthma and allergy medication. Take in the evening for best effect.'
            },
            {
                'name': 'Fluticasone',
                'category': 'Corticosteroid Nasal Spray',
                'dosage': '50mcg/spray',
                'species_applicable': 'Humans',
                'notes': 'Nasal steroid for allergic rhinitis. Use daily for best results.'
            },
        ]

        # Create medicine objects
        created_count = 0
        for medicine_data in medicines_data:
            medicine, created = Medicine.objects.get_or_create(
                name=medicine_data['name'],
                defaults=medicine_data
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} medicines in the database.'
            )
        )
