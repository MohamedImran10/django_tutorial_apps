from django.shortcuts import render,HttpResponse
from .forms import CalculatorForm

# Create your views here.
def calculator_view(request):
    result=None
    if request.method =="POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1=form.cleaned_data['num1']
            num2=form.cleaned_data['num2']
            
            operation = form.cleaned_data['operation']
            
            if operation =='add':
                result=num1+num2
            elif operation == 'subtract':
                result=num1-num2
            elif operation == 'multiply':
                result=num1*num2
            elif operation == 'div':
                if num2 == 0:
                    result="Division by zero is not possible."
                else:
                    result=num1/num2
                    result="{:.2f}".format(result)
            elif operation == 'moddiv':
                if num2 == 0:
                    result="Modulus by zero is not possible."
                else:   
                    result=num1%num2
    else:
        form = CalculatorForm()
    
    return render(request ,'calc.html' ,{'form' : form ,'result':result})

def quit_view(request):
    return HttpResponse("Thanks for using the calculator.You can close this window.")
    

                              