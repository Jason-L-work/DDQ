from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})  # <-- This is what Django tries to load


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm  # assuming you have a form for profile editing

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # or wherever you want to redirect
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/edit_profile.html', {'form': form})
