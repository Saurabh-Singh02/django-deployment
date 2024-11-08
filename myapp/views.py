from django.shortcuts import render, get_object_or_404
from .models import Profile, Skill, Project, Experience, Education, ContactMessage
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm

# Main portfolio page view
def portfolio_home(request):
    profile = get_object_or_404(Profile, id=1)  # Assuming one profile
    skills = Skill.objects.filter(profile=profile)
    projects = Project.objects.filter(profile=profile)
    experiences = Experience.objects.filter(profile=profile)
    education = Education.objects.filter(profile=profile)
    
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'education': education
    }
    return render(request, 'home.html', context)

# Project details view
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})

# Contact page view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves contact message
            return HttpResponseRedirect(reverse('myapp:contact'))
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
