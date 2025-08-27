import os
import joblib
from django.conf import settings
from django.shortcuts import render,redirect





# Path to the model file
MODEL_PATH = os.path.join(settings.BASE_DIR, 'loan_approval', 'model', 'tree_model')

# Load the model
model = joblib.load(MODEL_PATH)

# Example function to use the model
hello="I am Hassan"
# Create your views here.
def home(request):
    if request.method == "POST":
        no_of_dependents = int(request.POST.get("no_of_dependents"))
        education = request.POST.get("education")
        self_employed = request.POST.get("self_employed")
        income_annum = request.POST.get("income_annum", "0")  # default to '0' if empty
        income_annum = int(income_annum)
        loan_amount = int(request.POST.get("loan_amount"))
        loan_term = int(request.POST.get("loan_term"))
        residential_assets_value = int(request.POST.get("residential_assets_value"))
        commercial_assets_value = int(request.POST.get("commercial_assets_value"))
        luxury_assets_value = int(request.POST.get("luxury_assets_value"))
        bank_asset_value = int(request.POST.get("bank_asset_value"))

        if self_employed == 'yes':
            self_employed = int(1)
        else:
            self_employed = int(0)

        if education == 'graduate':
            education = int(1)
        else:
            education = int(0)
        
        
           
            features = [[no_of_dependents, self_employed, education, income_annum, loan_amount, loan_term, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value]]
            value = model.predict(features)
            if value == 0:
                result = "Congratulations! Your loan is likely to be approved."
            else:
                result = "We regret to inform you that your loan application has been denied."
                
            # print(income_annum, no_of_dependents, loan_amount, loan_term, education, self_employed, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value)
            
            
            return redirect("result", result)

    return render(request, "index.html")

def result(request, result):

    return render(request, "result.html",{'result': result})