import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here-change-this-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'comparative_medicine_database.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'comparative_medicine_database.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Heroku: Update database configuration from $DATABASE_URL
import dj_database_url
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=500,
        conn_health_checks=True,
    )

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Create the static directories if they don't exist
STATICFILES_DIRS = []
if (BASE_DIR / 'static').exists():
    STATICFILES_DIRS.append(BASE_DIR / 'static')

# WhiteNoise configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


<!-- Add this to your index.html file in the <script> section -->
<script>
// Clear all search fields and filters when page loads
document.addEventListener('DOMContentLoaded', function() {
    clearAllFieldsOnPageLoad();
});

// Function to clear all fields when page loads/refreshes
function clearAllFieldsOnPageLoad() {
    // Clear the medicine dropdown
    const medicineSelect = document.getElementById('medicineSelect');
    if (medicineSelect) {
        medicineSelect.value = '';
    }
    
    // Clear category filter
    const categoryFilter = document.getElementById('categoryFilter');
    if (categoryFilter) {
        categoryFilter.value = '';
    }
    
    // Clear species filter
    const speciesFilter = document.getElementById('speciesFilter');
    if (speciesFilter) {
        speciesFilter.value = '';
    }
    
    // Clear search input
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.value = '';
    }
    
    // Clear patient information form
    const patientForm = document.getElementById('patientInfoForm');
    if (patientForm) {
        patientForm.reset();
    }
    
    // Hide the selected medicine details section
    const addToCartSection = document.getElementById('addToCartSection');
    if (addToCartSection) {
        addToCartSection.style.display = 'none';
    }
    
    // Reset all medicine cards to visible
    const medicineCards = document.querySelectorAll('.medicine-card');
    medicineCards.forEach(card => {
        card.style.display = 'block';
    });
    
    // Clear any active filter states
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Activate "All" buttons if they exist
    document.querySelectorAll('.filter-btn[data-filter="all"]').forEach(btn => {
        btn.classList.add('active');
    });
}

// Function to remove random prices completely
function updateAddToCartSection(medicine) {
    document.getElementById('selectedMedicineName').textContent = medicine.name;
    document.getElementById('selectedMedicineCategory').textContent = medicine.category;
    document.getElementById('selectedMedicineSpecies').textContent = medicine.species || medicine.species_applicable || 'Human';
    document.getElementById('selectedMedicineDosage').textContent = medicine.dosage;
    
    // USE ONLY THE MEDICINE'S ACTUAL PRICE - NO RANDOM GENERATION!
    let price = medicine.price;
    
    // If no price in medicine object, use fixed prices by name
    if (!price) {
        switch(medicine.name) {
            case 'Aspirin':
                price = 4.99;
                break;
            case 'Ibuprofen':
                price = 5.49;
                break;
            case 'Acetaminophen':
                price = 3.99;
                break;
            case 'Vitamin C':
                price = 6.99;
                break;
            case 'Daily Multivitamin':
                price = 8.99;
                break;
            case 'Loratadine':
                price = 6.49;
                break;
            default:
                price = 4.99;
        }
    }
    
    document.getElementById('selectedMedicinePrice').textContent = price.toFixed(2);
    
    // Get comprehensive formula data
    const formulaData = getComprehensiveFormulaData(medicine.name);
    
    // Update formula information
    document.getElementById('molecularFormula').textContent = formulaData.molecularFormula;
    document.getElementById('molecularWeight').textContent = formulaData.molecularWeight;
    document.getElementById('chemicalName').textContent = formulaData.chemicalName;
    document.getElementById('mechanismOfAction').textContent = formulaData.mechanismOfAction;
    document.getElementById('therapeuticClass').textContent = formulaData.therapeuticClass;
    document.getElementById('routeOfAdmin').textContent = formulaData.routeOfAdmin;
    document.getElementById('absorption').textContent = formulaData.absorption;
    document.getElementById('distribution').textContent = formulaData.distribution;
    document.getElementById('metabolism').textContent = formulaData.metabolism;
    document.getElementById('elimination').textContent = formulaData.elimination;
    document.getElementById('contraindications').textContent = formulaData.contraindications;
    document.getElementById('sideEffects').textContent = formulaData.sideEffects;
    
    // Show the add to cart section
    document.getElementById('addToCartSection').style.display = 'block';
    
    // Store medicine data with FIXED price
    window.selectedMedicineData = {
        id: medicine.id,
        name: medicine.name,
        category: medicine.category,
        dosage: medicine.dosage,
        species_applicable: medicine.species || medicine.species_applicable || 'Human',
        price: parseFloat(price), // Use the fixed price
        notes: medicine.notes || medicine.description
    };
}

// Function to clear all filters (for manual clearing)
function clearAllFilters() {
    clearAllFieldsOnPageLoad();
}

// Make sure your humanMedicines array has fixed prices
const humanMedicines = [
    {
        id: 'aspirin_human',
        name: 'Aspirin',
        category: 'analgesic',
        species: 'human',
        dosage: '325-650mg every 4-6 hours',
        price: 4.99, // Fixed price
        notes: 'Over-the-counter pain reliever and anti-inflammatory.'
    },
    {
        id: 'ibuprofen_human',
        name: 'Ibuprofen',
        category: 'analgesic',
        species: 'human',
        dosage: '200-400mg every 6-8 hours',
        price: 5.49, // Fixed price
        notes: 'Non-steroidal anti-inflammatory drug (NSAID).'
    },
    {
        id: 'acetaminophen_human',
        name: 'Acetaminophen',
        category: 'analgesic',
        species: 'human',
        dosage: '500-1000mg every 6-8 hours',
        price: 3.99, // Fixed price
        notes: 'Pain reliever and fever reducer.'
    }
    // Add more medicines with fixed prices
];
</script>

<!-- Update your search inputs in index.html -->
<input type="text" class="form-control" id="searchInput" placeholder="Search medicines..." autocomplete="off">

<select class="form-select" id="medicineSelect" autocomplete="off">
    <option value="">Select a medicine...</option>
</select>

<select class="form-select" id="categoryFilter" autocomplete="off">
    <option value="">All Categories</option>
</select>

<select class="form-select" id="speciesFilter" autocomplete="off">
    <option value="">All Species</option>
</select>