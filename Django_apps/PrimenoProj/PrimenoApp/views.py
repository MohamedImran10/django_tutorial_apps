from django.shortcuts import render
from .forms import NumberForm

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True
                
def input_view(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            primes = [num for num in range(2, number + 1) if is_prime(num)]  # Corrected range function
            
            return render(request, 'result.html', {'number': number, 'primes': primes})
        
    else:
        form = NumberForm()
        
    return render(request, 'index.html', {'form': form})
