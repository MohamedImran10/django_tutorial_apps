from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def input_view(request):
    if request.method == "POST":
        
        user_input1=int(request.POST.get('user_input1'))
        user_input2=int(request.POST.get('user_input2'))
        
        #print("User input 1:",user_input1)
        #print("User input 2:",user_input2)
    

        return HttpResponse("Addition of two numbers : %d"%(user_input1+user_input2))
    
    return render(request,'input_form.html')
    