from itertools import groupby

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Experience, Profile, Project, Service, Skill, SocialLink


def _grouped_skills():
    """Group skills by their category, preserving the model's default order."""
    skills = Skill.objects.all()
    category_labels = dict(Skill.CATEGORY_CHOICES)
    groups = []
    for key, items in groupby(skills, key=lambda s: s.category):
        groups.append({"label": category_labels.get(key, key), "items": list(items)})
    return groups


def index(request):
    profile = Profile.objects.first()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks -- your message is in. I'll get back to you soon.")
            return redirect(f"{request.path}#contact")
    else:
        form = ContactForm()

    context = {
        "profile": profile,
        "skill_groups": _grouped_skills(),
        "projects": Project.objects.all(),
        "experience": Experience.objects.all(),
        "services": Service.objects.all(),
        "social_links": SocialLink.objects.all(),
        "contact_form": form,
    }
    return render(request, "portfolio/index.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    profile = Profile.objects.first()
    return render(
        request,
        "portfolio/project_detail.html",
        {"project": project, "profile": profile},
    )
