import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="Owoeye Fiyinfoluwa Orire", max_length=120)),
                ("title", models.CharField(default="Full-Stack Developer & Software Engineer", max_length=200)),
                ("tagline", models.TextField()),
                ("about", models.TextField()),
                ("location", models.CharField(blank=True, max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=40)),
                ("years_experience", models.PositiveSmallIntegerField(default=1)),
                ("projects_completed", models.PositiveSmallIntegerField(default=0)),
                ("avatar", models.ImageField(blank=True, null=True, upload_to="profile/")),
                ("resume", models.FileField(blank=True, null=True, upload_to="resume/")),
            ],
            options={"verbose_name": "Profile", "verbose_name_plural": "Profile"},
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=60)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("language", "Languages & Frameworks"),
                            ("database", "Databases"),
                            ("tools", "Tools & Practices"),
                            ("other", "Other"),
                        ],
                        default="language",
                        max_length=20,
                    ),
                ),
                ("proficiency", models.PositiveSmallIntegerField(default=80)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["category", "order", "name"]},
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("summary", models.CharField(max_length=240)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="projects/")),
                ("tech_stack", models.CharField(max_length=300)),
                ("features", models.TextField(blank=True)),
                ("github_url", models.URLField(blank=True)),
                ("live_url", models.URLField(blank=True)),
                ("featured", models.BooleanField(default=False)),
                ("order", models.PositiveIntegerField(default=0)),
                ("year", models.CharField(blank=True, max_length=20)),
            ],
            options={"ordering": ["-featured", "order", "-id"]},
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("role", models.CharField(max_length=150)),
                ("organisation", models.CharField(max_length=150)),
                ("location", models.CharField(blank=True, max_length=120)),
                ("start_date", models.CharField(max_length=40)),
                ("end_date", models.CharField(blank=True, max_length=40)),
                ("description", models.TextField()),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "-id"]},
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField()),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "platform",
                    models.CharField(
                        choices=[
                            ("email", "Email"),
                            ("github", "GitHub"),
                            ("linkedin", "LinkedIn"),
                            ("telegram", "Telegram"),
                            ("whatsapp", "WhatsApp"),
                            ("twitter", "X / Twitter"),
                            ("other", "Other"),
                        ],
                        default="other",
                        max_length=20,
                    ),
                ),
                ("label", models.CharField(max_length=60)),
                ("url", models.CharField(max_length=300)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("read", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-created"]},
        ),
    ]
