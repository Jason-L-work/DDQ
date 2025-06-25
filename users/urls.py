# users/urls.py
from django.urls import path
from .views import profile_view

urlpatterns = [
    path('profile/', profile_view, name='profile'),
]




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'profile': request.user.userprofile
    })

@login_required
def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})
