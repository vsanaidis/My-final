from django.shortcuts import render, redirect
from .forms import SignupForm
# I create the user signup view
def user_signup(request):
    if request.method == 'POST':# if the form is submitted, this is what POST means
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Update this to the name of your login URL
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form} )
