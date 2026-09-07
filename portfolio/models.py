from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Profile(models.Model):
    """Singleton-style model — there should only ever be one row.
    Edit it from /admin/portfolio/profile/."""

    name = models.CharField(max_length=120, default="Owoeye Fiyinfoluwa Orire")
    title = models.CharField(
        max_length=200,
        default="Full-Stack Developer & Software Engineer",
        help_text="Shown right under your name on the homepage.",
    )
    tagline = models.TextField(
        help_text="Short 1–2 sentence introduction shown in the hero section."
    )
    about = models.TextField(help_text="Longer paragraph(s) for the About section.")
    location = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    years_experience = models.PositiveSmallIntegerField(default=1)
    projects_completed = models.PositiveSmallIntegerField(default=0)
    avatar = models.ImageField(upload_to="profile/", blank=True, null=True)
    resume = models.FileField(upload_to="resume/", blank=True, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("language", "Languages & Frameworks"),
        ("database", "Databases"),
        ("tools", "Tools & Practices"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="language")
    proficiency = models.PositiveSmallIntegerField(
        default=80, help_text="0–100. Drives the fill level of the skill meter."
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.CharField(max_length=240, help_text="One-line summary shown on the card.")
    description = models.TextField(help_text="Full description shown on hover/expand or detail view.")
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    tech_stack = models.CharField(
        max_length=300, help_text="Comma-separated, e.g. Django, PostgreSQL, HTMX"
    )
    features = models.TextField(
        blank=True, help_text="One feature per line — shown as a bullet list."
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False, help_text="Featured projects are pinned to the top.")
    order = models.PositiveIntegerField(default=0)
    year = models.CharField(max_length=20, blank=True, help_text="e.g. 2026 or 'Ongoing'")

    class Meta:
        ordering = ["-featured", "order", "-id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project_detail", args=[self.slug])

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]

    def feature_list(self):
        return [f.strip() for f in self.features.splitlines() if f.strip()]


class Experience(models.Model):
    role = models.CharField(max_length=150)
    organisation = models.CharField(max_length=150)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.CharField(max_length=40, help_text="e.g. June 2025")
    end_date = models.CharField(
        max_length=40, blank=True, help_text="Leave blank to show 'Present'."
    )
    description = models.TextField(help_text="One bullet point per line.")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return f"{self.role} — {self.organisation}"

    def bullet_list(self):
        return [line.strip() for line in self.description.splitlines() if line.strip()]

    def period(self):
        return f"{self.start_date} – {self.end_date or 'Present'}"


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ("email", "Email"),
        ("github", "GitHub"),
        ("linkedin", "LinkedIn"),
        ("telegram", "Telegram"),
        ("whatsapp", "WhatsApp"),
        ("twitter", "X / Twitter"),
        ("other", "Other"),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default="other")
    label = models.CharField(max_length=60, help_text="Text shown to visitors, e.g. 'GitHub'")
    url = models.CharField(
        max_length=300,
        help_text="Full URL, or mailto:/tel: link, e.g. mailto:you@example.com",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.label


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} <{self.email}> — {self.created:%Y-%m-%d}"
