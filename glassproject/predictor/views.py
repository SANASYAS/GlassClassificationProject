from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ml_model import predict_glass_type

@api_view(['POST'])
def predict_view(request):
    data = request.data.get('features')
    if data:
        prediction = predict_glass_type(data)
        return Response({'prediction': int(prediction)})
    return Response({'error': 'No input data provided'}, status=400)


GLASS_TYPE_MAPPING = {
    1: "building_windows_float_processed",
    2: "building_windows_non_float_processed",
    3: "vehicle_windows_float_processed",
    4: "vehicle_windows_non_float_processed (none in this database)",
    5: "containers",
    6: "tableware",
    7: "headlamps"
}

def glass_form_view(request):
    if request.method == 'POST':
        features = [
            float(request.POST['RI']),
            float(request.POST['Na']),
            float(request.POST['Mg']),
            float(request.POST['Al']),
            float(request.POST['Si']),
            float(request.POST['K']),
            float(request.POST['Ca']),
            float(request.POST['Ba']),
            float(request.POST['Fe']),
        ]
        prediction = predict_glass_type(features)
        prediction = int(prediction)  # Ensure it's an integer
        glass_name = GLASS_TYPE_MAPPING.get(prediction, "Unknown")

        return render(request, 'predictor/result.html', {'prediction': glass_name})

    return render(request, 'predictor/form.html')
