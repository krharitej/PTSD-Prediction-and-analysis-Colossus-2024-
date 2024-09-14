from django.shortcuts import render
import joblib
import numpy as np

def home_view(request):
    return render(request, 'play/index.html')

def about_view(request):
    return render(request, 'play/about.html')

def appointment_view(request):
    return render(request, 'play/appointment.html')

def contact_view(request):
    return render(request, 'play/contact.html')

def team_view(request):
    return render(request, 'play/team.html')

def predict_view(request):
    if request.method == 'POST':
        # HTML form fields
        nightmare = float(request.POST.get('nightmare'))
        flashback = float(request.POST.get('flashback'))
        avoidance = float(request.POST.get('avoidance'))
        hypervigilance = float(request.POST.get('hypervigilance'))
        emotionalNumbing = float(request.POST.get('emotionalNumbing'))
        anxiety = float(request.POST.get('anxiety'))

        # Prepare the data for the model
        input_data = np.array([[nightmare, flashback, avoidance, hypervigilance, emotionalNumbing, anxiety]])  # Add other features as needed

        # Load model
        model0 = joblib.load('random_forest_therapy_model.joblib')
        model1 = joblib.load('random_forest_trauma_model.joblib')

        # prediction
        prediction = model0.predict(input_data)
        prediction2 = model1.predict(input_data)

        trauma_level_dict = {0: 'Mild', 1: 'Moderate', 2: 'Severe'}
        therapy_dict = {0: 'CBT', 1: 'Exposure Therapy', 2: 'others'}
        prediction = trauma_level_dict[prediction[0]]
        prediction2 = therapy_dict[prediction2[0]]

        # output result
        return render(request, 'play/result.html', {'prediction': prediction, 'prediction2': prediction2})

    return render(request, 'play/blog.html')
