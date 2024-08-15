from django.shortcuts import render

# Create your views here.
def input_view(request):
    if request.method == 'POST':
        # Use get() with default values to avoid KeyError if the key is missing
        try:
            user_input1 = int(request.POST.get('user_input1', 0))
            user_input2 = int(request.POST.get('user_input2', 0))
        except ValueError:
            # Handle the case where input values are not integers
            context = {
                'error': 'Please enter valid integers for both inputs.'
            }
            return render(request, 'input.html', context)

        # Perform calculations
        value1 = user_input1 + user_input2
        value2 = user_input1 - user_input2
        value3 = user_input1 * user_input2
        if user_input2 !=0:
            value4 = user_input1 / user_input2 
            value4 = "{:.2f}".format(value4)
        else:
            value4 = "Divsion by Zero error"
        # Format value4 to two decimal places if it's not None
        
        
        context = {
            'input1': user_input1,
            'input2': user_input2,
            'addition': value1,
            'difference': value2,
            'multiplication': value3,
            'division': value4,
        }
        
        return render(request, 'output.html', context)
    
    # If the request is GET, simply render the input page
    return render(request, 'input.html')
