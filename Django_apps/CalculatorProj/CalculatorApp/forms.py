from django import forms

class CalculatorForm(forms.Form):
    num1=forms.IntegerField(label="Enter First number :")
    num2=forms.IntegerField(label="Enter Second number :")
    
    OPERATION_CHOICES = [
        ('add','Addition'),
        ('subtract','Subtraction'),
        ('multiply','Multiplication'),
        ('div','Division'),
        ('moddiv','ModDivision')   
    ]
    
    operation = forms.ChoiceField(choices=OPERATION_CHOICES)
    
    

        
    
    