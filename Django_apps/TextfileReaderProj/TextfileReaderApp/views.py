import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def read_text(request):
    file_path = os.path.join(settings.BASE_DIR, 'files', 'file_name.txt')
    
    if request.method == 'POST':
        new_content = request.POST.get('content', '')
        
        if new_content:
            try:
                # Ensure the directory exists
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                with open(file_path, 'a+') as file:
                    file.write(new_content + '\n')
                    file.seek(0)  # Move to the beginning of the file
                    content = file.read()
                    return HttpResponse(content, content_type='text/plain')
            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}", status=500)
    
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'r') as file:
            content = file.read()
            return HttpResponse(content, content_type='text/plain')
        
    except FileNotFoundError:
        return HttpResponse('File not found', status=404)
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

def form_view(request):
    return render(request, 'form.html')
