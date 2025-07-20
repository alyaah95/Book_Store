

# Create your views here.


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login 

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            return redirect(reverse_lazy('bookstore:list-books')) 

    else: 
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})