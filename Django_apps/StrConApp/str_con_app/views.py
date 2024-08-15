from django.shortcuts import render,HttpResponse
from .forms import StrConForm


# Create your views here.
def str_con_view(request):
    
    result=None
    
    if request.method == 'POST':
        form= StrConForm(request.POST)
        
        if form.is_valid():
            input_string=form.cleaned_data['input_string']
            case_choice=form.cleaned_data['case_choice']
            
            if case_choice == 'upper':
                result = input_string.upper()
            elif case_choice == 'title':
                result = input_string.title()
            elif case_choice == 'lower':
                result = input_string.lower()
            elif case_choice == 'sentence':
                result= input_string.capitalize()
    
    else:
        form = StrConForm
        
    return render(request,'converter.html',{'form':form,'result':result})

def quit_view(request):
    return HttpResponse("Thank you for using string converter .You can close this window")




                