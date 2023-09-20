from datetime import timezone
from django.shortcuts import render,redirect
from checker_palindromo.forms import PalindromeForm
from checker_palindromo.models import Words
def checker (word):
    word = word.lower().replace(' ', '')
    return word == word[::-1]
      

# Create your views here.
def created_at(request):
    form = PalindromeForm(request.POST or None)
    if form.is_valid():
        word = form.cleaned_data['descrip']

        already_created = Words.objects.filter(descrip=word)

        if already_created:
            already_created.date_created = timezone.now()
            already_created.save()
        else:
            form.save()

        return redirect('verificador.html')
    return render(request, 'words/created_at.html', {'form': form})

def update_at(request,code):
    register = Words.objects.get(code=code)
    form = PalindromeForm(request.POST, instance=register)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('verificador.html')

    return render(request, 'words/update_at.html', {'form':form})

def delete_at(request,code):
    word = Words.objects.get(code=code)
    word.delete()
    return redirect('verificador.html')

def bienvenido(request):
    return render(request, 'bienvenido.html')


def verificador(request):
    words = Words.objects.all()
    return render(request,'words/verificador.html', {'words': words})

def verification(request,code):
    word = Words.objects.get(code=code)
    verify = checker(word.descrip)
    if verify:
        result = "It is a palindrome"
    else:
        result = "It is not a palindrome"
    return render(request,'words/verification.html', {'word': word, 'result': result})
    