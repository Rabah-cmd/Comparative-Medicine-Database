#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from comparative_medicine_database.models import Medicine

def populate_medicines():
    """Populate the database with human medicines data"""
    
    # Clear existing data
    Medicine.objects.all().delete()
    print("Cleared existing medicine data.")
    
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
        # Animal/Veterinary Medicines
        {
            'name': 'Carprofen',
            'category': 'NSAID',
            'dosage': '25mg, 75mg, 100mg tablets',
            'species_applicable': 'Dogs',
            'notes': 'Pain relief and anti-inflammatory for dogs. Monitor for GI upset and liver function.'
        },
        {
            'name': 'Meloxicam',
            'category': 'NSAID',
            'dosage': '0.5mg/mL oral suspension',
            'species_applicable': 'Cats, Dogs',
            'notes': 'Non-steroidal anti-inflammatory for cats and dogs. Use with caution in cats.'
        },
        {
            'name': 'Enrofloxacin',
            'category': 'Fluoroquinolone Antibiotic',
            'dosage': '22.7mg, 68mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Broad-spectrum antibiotic for bacterial infections in small animals.'
        },
        {
            'name': 'Phenylbutazone',
            'category': 'NSAID',
            'dosage': '1g, 2g tablets/paste',
            'species_applicable': 'Horses',
            'notes': 'Anti-inflammatory for horses. Monitor for blood dyscrasias with long-term use.'
        },
        {
            'name': 'Banamine (Flunixin)',
            'category': 'NSAID',
            'dosage': '250mg/mL injection',
            'species_applicable': 'Horses, Cattle',
            'notes': 'Pain relief and anti-inflammatory for large animals. Effective for colic in horses.'
        },
        {
            'name': 'Ivermectin',
            'category': 'Antiparasitic',
            'dosage': '1.87% paste, 1% injection',
            'species_applicable': 'Horses, Cattle, Sheep, Pigs',
            'notes': 'Broad-spectrum dewormer for internal and external parasites.'
        },
        {
            'name': 'Revolution (Selamectin)',
            'category': 'Topical Antiparasitic',
            'dosage': '6% topical solution',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Monthly flea, tick, and heartworm prevention for dogs and cats.'
        },
        {
            'name': 'Heartgard (Ivermectin)',
            'category': 'Heartworm Preventive',
            'dosage': '68mcg, 136mcg, 272mcg chewables',
            'species_applicable': 'Dogs',
            'notes': 'Monthly heartworm prevention for dogs. Also treats roundworms and hookworms.'
        },
        {
            'name': 'Adequan (Polysulfated GAG)',
            'category': 'Joint Supplement',
            'dosage': '100mg/mL injection',
            'species_applicable': 'Dogs, Horses',
            'notes': 'Injectable joint supplement for arthritis and joint health.'
        },
        {
            'name': 'Gabapentin',
            'category': 'Neuropathic Pain',
            'dosage': '100mg, 300mg capsules',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Pain management for neuropathic pain and anxiety in small animals.'
        },
        {
            'name': 'Tramadol',
            'category': 'Opioid Analgesic',
            'dosage': '50mg tablets',
            'species_applicable': 'Dogs',
            'notes': 'Pain medication for moderate to severe pain in dogs.'
        },
        {
            'name': 'Prednisolone',
            'category': 'Corticosteroid',
            'dosage': '5mg, 20mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Anti-inflammatory steroid for allergies, autoimmune conditions, and inflammation.'
        },
        {
            'name': 'Furosemide',
            'category': 'Diuretic',
            'dosage': '12.5mg, 50mg tablets',
            'species_applicable': 'Dogs, Cats, Horses',
            'notes': 'Loop diuretic for heart failure and fluid retention in animals.'
        },
        {
            'name': 'Digoxin',
            'category': 'Cardiac Glycoside',
            'dosage': '0.125mg, 0.25mg tablets',
            'species_applicable': 'Dogs',
            'notes': 'Heart medication for congestive heart failure and arrhythmias in dogs.'
        },
        {
            'name': 'Enalapril',
            'category': 'ACE Inhibitor',
            'dosage': '2.5mg, 5mg, 10mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Heart and kidney medication for hypertension and heart failure.'
        },
        {
            'name': 'Amoxicillin/Clavulanate',
            'category': 'Antibiotic',
            'dosage': '62.5mg, 125mg, 250mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Broad-spectrum antibiotic combination for resistant bacterial infections.'
        },
        {
            'name': 'Clindamycin',
            'category': 'Antibiotic',
            'dosage': '25mg, 75mg, 150mg capsules',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Antibiotic effective against anaerobic bacteria and some protozoa.'
        },
        {
            'name': 'Metronidazole',
            'category': 'Antibiotic/Antiprotozoal',
            'dosage': '250mg, 500mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Antibiotic for anaerobic infections and GI protozoal infections.'
        },
        {
            'name': 'Cerenia (Maropitant)',
            'category': 'Antiemetic',
            'dosage': '16mg, 24mg, 60mg, 160mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Anti-nausea medication for motion sickness and chemotherapy-induced vomiting.'
        },
        {
            'name': 'Famotidine',
            'category': 'H2 Receptor Antagonist',
            'dosage': '10mg, 20mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Acid reducer for gastric ulcers and acid reflux in small animals.'
        },
        {
            'name': 'Sucralfate',
            'category': 'Gastric Protectant',
            'dosage': '1g tablets',
            'species_applicable': 'Dogs, Cats, Horses',
            'notes': 'Gastric ulcer treatment that forms protective barrier over ulcerated tissue.'
        },
        {
            'name': 'Lactulose',
            'category': 'Laxative/Hepatic Encephalopathy',
            'dosage': '10g/15mL syrup',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Osmotic laxative and treatment for hepatic encephalopathy.'
        },
        {
            'name': 'Azithromycin',
            'category': 'Macrolide Antibiotic',
            'dosage': '250mg, 500mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Antibiotic for respiratory and soft tissue infections.'
        },
        {
            'name': 'Dexamethasone',
            'category': 'Corticosteroid',
            'dosage': '0.25mg, 0.5mg, 0.75mg, 4mg tablets',
            'species_applicable': 'Dogs, Cats, Horses, Cattle',
            'notes': 'Potent anti-inflammatory steroid for various inflammatory conditions.'
        },
        {
            'name': 'Atipamezole',
            'category': 'Alpha-2 Antagonist',
            'dosage': '5mg/mL injection',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Reversal agent for dexmedetomidine sedation.'
        },
        {
            'name': 'Butorphanol',
            'category': 'Opioid Analgesic',
            'dosage': '0.5mg, 1mg, 5mg, 10mg tablets',
            'species_applicable': 'Dogs, Cats, Horses',
            'notes': 'Pain medication and antitussive for animals.'
        },
        {
            'name': 'Ketamine',
            'category': 'Dissociative Anesthetic',
            'dosage': '100mg/mL injection',
            'species_applicable': 'Dogs, Cats, Horses, Exotic Animals',
            'notes': 'Injectable anesthetic for procedures and pain management.'
        },
        {
            'name': 'Acepromazine',
            'category': 'Phenothiazine Tranquilizer',
            'dosage': '10mg, 25mg tablets',
            'species_applicable': 'Dogs, Cats, Horses',
            'notes': 'Sedative and anti-anxiety medication for animals.'
        },
        {
            'name': 'Trazodone',
            'category': 'Serotonin Antagonist',
            'dosage': '50mg, 100mg, 150mg tablets',
            'species_applicable': 'Dogs',
            'notes': 'Anti-anxiety medication for behavioral issues in dogs.'
        },
        {
            'name': 'Fluoxetine',
            'category': 'SSRI',
            'dosage': '10mg, 20mg capsules',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Antidepressant for separation anxiety and behavioral disorders.'
        },
        {
            'name': 'Levothyroxine',
            'category': 'Thyroid Hormone',
            'dosage': '0.1mg, 0.2mg, 0.3mg, 0.4mg, 0.5mg tablets',
            'species_applicable': 'Dogs',
            'notes': 'Thyroid hormone replacement for hypothyroidism in dogs.'
        },
        {
            'name': 'Methimazole',
            'category': 'Antithyroid',
            'dosage': '2.5mg, 5mg tablets',
            'species_applicable': 'Cats',
            'notes': 'Treatment for hyperthyroidism in cats.'
        },
        {
            'name': 'Insulin Glargine',
            'category': 'Long-acting Insulin',
            'dosage': '100 units/mL injection',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Long-acting insulin for diabetes management in pets.'
        },
        {
            'name': 'ProZinc (Protamine Zinc Insulin)',
            'category': 'Intermediate-acting Insulin',
            'dosage': '40 units/mL injection',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Veterinary insulin specifically formulated for cats and dogs.'
        },
        {
            'name': 'Pimobendan',
            'category': 'Inodilator',
            'dosage': '1.25mg, 2.5mg, 5mg chewables',
            'species_applicable': 'Dogs',
            'notes': 'Heart medication for congestive heart failure and dilated cardiomyopathy.'
        },
        {
            'name': 'Sildenafil',
            'category': 'Phosphodiesterase Inhibitor',
            'dosage': '20mg tablets',
            'species_applicable': 'Dogs',
            'notes': 'Treatment for pulmonary hypertension in dogs.'
        },
        {
            'name': 'Trilostane',
            'category': 'Adrenal Steroid Inhibitor',
            'dosage': '10mg, 30mg, 60mg, 120mg capsules',
            'species_applicable': 'Dogs',
            'notes': 'Treatment for Cushing\'s disease (hyperadrenocorticism) in dogs.'
        },
        {
            'name': 'Mitotane',
            'category': 'Adrenolytic',
            'dosage': '500mg tablets',
            'species_applicable': 'Dogs',
            'notes': 'Treatment for Cushing\'s disease and adrenal tumors in dogs.'
        },
        {
            'name': 'Cyclosporine',
            'category': 'Immunosuppressant',
            'dosage': '10mg, 25mg, 50mg, 100mg capsules',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Immunosuppressive therapy for autoimmune conditions and organ transplants.'
        },
        {
            'name': 'Azathioprine',
            'category': 'Immunosuppressant',
            'dosage': '50mg tablets',
            'species_applicable': 'Dogs',
            'notes': 'Immunosuppressive medication for autoimmune diseases. Not recommended for cats.'
        },
        {
            'name': 'Chlorambucil',
            'category': 'Alkylating Agent',
            'dosage': '2mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Chemotherapy drug for lymphoma and other cancers.'
        },
        {
            'name': 'Carboplatin',
            'category': 'Platinum Compound',
            'dosage': '50mg, 150mg, 450mg injection',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Chemotherapy drug for various cancers in veterinary oncology.'
        },
        {
            'name': 'Fenbendazole',
            'category': 'Anthelmintic',
            'dosage': '22.2% granules',
            'species_applicable': 'Dogs, Cats, Horses, Cattle, Sheep, Goats',
            'notes': 'Broad-spectrum dewormer for various internal parasites.'
        },
        {
            'name': 'Praziquantel',
            'category': 'Anthelmintic',
            'dosage': '23mg, 34mg tablets',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Treatment for tapeworms in dogs and cats.'
        },
        {
            'name': 'Pyrantel Pamoate',
            'category': 'Anthelmintic',
            'dosage': '22.7mg/mL suspension',
            'species_applicable': 'Dogs, Cats, Horses',
            'notes': 'Dewormer for roundworms and hookworms.'
        },
        {
            'name': 'Fipronil',
            'category': 'Topical Insecticide',
            'dosage': '9.8% topical solution',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Flea and tick prevention and treatment.'
        },
        {
            'name': 'Imidacloprid',
            'category': 'Topical Insecticide',
            'dosage': '10% topical solution',
            'species_applicable': 'Dogs, Cats',
            'notes': 'Flea prevention and treatment for dogs and cats.'
        },
        {
            'name': 'Buprenorphine',
            'category': 'Opioid Analgesic',
            'dosage': '0.3mg/mL injection',
            'species_applicable': 'Dogs, Cats, Rabbits, Exotic Animals',
            'notes': 'Potent pain medication for moderate to severe pain.'
        },
        {
            'name': 'Morphine',
            'category': 'Opioid Analgesic',
            'dosage': '15mg/mL injection',
            'species_applicable': 'Dogs, Cats, Horses',
            'notes': 'Strong pain medication for severe pain management.'
        }
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
            print(f"Created: {medicine_data['name']}")

    print(f"\nSuccessfully created {created_count} medicines in the database.")
    print(f"Total medicines in database: {Medicine.objects.count()}")

if __name__ == '__main__':
    populate_medicines()
