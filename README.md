# Owoeye Fiyinfoluwa Orire — Portfolio

A full-stack Django portfolio site. Every section on the page — profile,
skills, projects, experience, services, and social links — is a database
model you edit from Django's built-in admin. No code changes needed to
update content.

## Setup

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_profile     # loads your real CV content as a starting point
python manage.py createsuperuser  # create your admin login
python manage.py runserver
```

Visit:
- **http://127.0.0.1:8000/** — the live site
- **http://127.0.0.1:8000/admin/** — the admin, log in with the superuser you created

## Editing content

Everything is editable from `/admin/`:

| Section on site | Admin model      | Notes |
|---|---|---|
| Hero / About     | **Profile**      | Singleton — one row only. Name, title, tagline, about text, contact info, stats. Upload an avatar/resume here too. |
| Skills           | **Skills**       | Each skill has a category and a 0–100 proficiency that drives the meter bar. |
| Projects         | **Projects**     | Upload a screenshot, write description/features (one per line), tech stack (comma-separated), GitHub/live links. Toggle "featured" to pin it. Each project gets its own detail page automatically. |
| Experience       | **Experience**   | One row per role. Description is one bullet per line. Leave "end date" blank to show "Present". |
| Services         | **Services**     | The service cards near the bottom of the page. |
| Contact links    | **Social links** | GitHub, LinkedIn, Telegram, WhatsApp, etc. Use `mailto:` or `tel:` prefixes where relevant. |
| Contact form submissions | **Contact messages** | Read-only log of everything submitted through the site's contact form. |

The `seed_profile` management command pre-loads your real CV content
(summary, work history, skills, services) plus a few **placeholder**
projects (FFX Market, Trading Bot, Banking/Asset Management, Apartment
Booking, Restaurant/Cafe) so the layout isn't empty — replace those with
your actual project screenshots, descriptions, and links from the admin.
Re-running the command is safe; it updates existing rows rather than
duplicating them.

## Design

The look is a dark, systems/dashboard aesthetic (deep charcoal-green
background, emerald accent, monospace for data-like labels) chosen to
suit backend/fintech-adjacent work like the trading bot and market
projects — not a generic template palette. Scroll-triggered reveal
animations and skill meters are handled by `portfolio/static/portfolio/js/main.js`
via `IntersectionObserver`, and respect `prefers-reduced-motion`.

## Structure

```
config/                 settings, root urls
portfolio/
  models.py             Profile, Skill, Project, Experience, Service, SocialLink, ContactMessage
  admin.py               admin registration for everything above
  forms.py               contact form
  views.py                homepage + project detail views
  management/commands/seed_profile.py   loads your real CV content
  templates/portfolio/   base.html, index.html, project_detail.html
  static/portfolio/      css/style.css, js/main.js
```

## Before deploying

`config/settings.py` currently has `DEBUG = True` and a placeholder
`SECRET_KEY` for local development. Before putting this on the internet:

1. Generate a real secret key and load it from an environment variable.
2. Set `DEBUG = False` and fill in `ALLOWED_HOSTS`.
3. Configure a real email backend if you want contact form submissions
   emailed to you (right now they're just saved and visible in `/admin/`
   under **Contact messages**).
4. Set up proper media file storage for uploaded project images (e.g.
   S3, Cloudinary) — the local `media/` folder is fine for development
   only.
5. Run `python manage.py collectstatic`.
