from django.core.management.base import BaseCommand

from portfolio.models import Experience, Profile, Project, Service, Skill, SocialLink


class Command(BaseCommand):
    help = "Seed the database with Owoeye Fiyinfoluwa Orire's real profile, skills, and experience."

    def handle(self, *args, **options):
        profile, _ = Profile.objects.update_or_create(
            id=1,
            defaults=dict(
                name="Owoeye Fiyinfoluwa Orire",
                title="Full-Stack Developer & Software Engineer",
                tagline=(
                    "I design and build backend systems and full-stack web "
                    "applications — from database models and REST APIs to "
                    "the interfaces people use every day."
                ),
                about=(
                    "I'm a backend-focused software developer with hands-on "
                    "experience building web applications in Python and "
                    "Django, including database modelling, authentication "
                    "systems, and CRUD application development. I've since "
                    "broadened into full-stack development with React, "
                    "Next.js, and Node.js, working remotely on a development "
                    "team.\n\n"
                    "I'm currently building an automated trading bot that "
                    "integrates external APIs, alongside ongoing freelance "
                    "backend projects. I bring a strong analytical "
                    "foundation from a BSc in Physics with Electronics, a "
                    "keen interest in API design and scalable backend "
                    "architecture, and a track record of working "
                    "independently and reliably in remote environments."
                ),
                location="Abuja, Nigeria",
                email="Ffoluwa5@gmail.com",
                phone="0810 573 7397",
                years_experience=2,
                projects_completed=6,
            ),
        )

        skills = [
            ("Python", "language", 90),
            ("Django", "language", 90),
            ("JavaScript", "language", 78),
            ("React", "language", 72),
            ("Next.js", "language", 70),
            ("Node.js", "language", 68),
            ("SQL / Relational DB Design", "database", 82),
            ("NoSQL Concepts", "database", 55),
            ("Git & GitHub", "tools", 85),
            ("REST API Design", "tools", 85),
            ("Testing & Debugging", "tools", 75),
            ("Data Analysis (Excel, Sheets)", "other", 65),
        ]
        for order, (name, category, proficiency) in enumerate(skills):
            Skill.objects.update_or_create(
                name=name,
                defaults=dict(category=category, proficiency=proficiency, order=order),
            )

        experience = [
            dict(
                role="Software Developer — Personal Project",
                organisation="Independent",
                start_date="May 2026",
                end_date="",
                order=0,
                description=(
                    "Developing a web application using Python and Django, building on "
                    "backend architecture and database design skills from previous roles\n"
                    "Designing and implementing RESTful API endpoints to support core "
                    "application features\n"
                    "Building database models and user authentication for the application\n"
                    "Testing and iterating on features as the project evolves"
                ),
            ),
            dict(
                role="Personal / Administrative Assistant",
                organisation="Independent",
                start_date="January 2026",
                end_date="May 2026",
                order=1,
                description=(
                    "Provided administrative and technical support to support business "
                    "operations\n"
                    "Managed documentation and scheduling for ongoing projects\n"
                    "Assisted with digital tasks and website updates\n"
                    "Supported research and data organisation for decision-making"
                ),
            ),
            dict(
                role="Full Stack Developer (Remote)",
                organisation="Spay Resources New World Limited",
                start_date="June 2025",
                end_date="December 2025",
                order=2,
                description=(
                    "Developed and maintained web application features using React, "
                    "Next.js, and Node.js\n"
                    "Built and integrated RESTful APIs to connect frontend interfaces "
                    "with backend services\n"
                    "Collaborated with a remote development team to plan, build, and "
                    "ship features on schedule\n"
                    "Implemented responsive UI components and resolved bugs to improve "
                    "application performance and reliability"
                ),
            ),
            dict(
                role="Digital Marketing & Website Manager",
                organisation="Independent / Freelance",
                start_date="January 2025",
                end_date="May 2025",
                order=3,
                description=(
                    "Managed website content and updates to keep information accurate "
                    "and current\n"
                    "Improved online visibility using digital marketing tools and "
                    "techniques\n"
                    "Monitored engagement metrics to inform content and outreach "
                    "decisions\n"
                    "Maintained business website systems and resolved day-to-day issues"
                ),
            ),
            dict(
                role="Freelance Software Developer (Python/Django)",
                organisation="Freelance",
                start_date="May 2024",
                end_date="",
                order=4,
                description=(
                    "Developed backend web applications for clients using Python and "
                    "Django\n"
                    "Designed database models and implemented authentication systems\n"
                    "Built CRUD applications and user management systems\n"
                    "Tested and optimised application performance"
                ),
            ),
        ]
        for item in experience:
            Experience.objects.update_or_create(
                role=item["role"], organisation=item["organisation"], defaults=item
            )

        services = [
            dict(
                title="Web Development",
                description="End-to-end web apps built with Django — from data model to deployed UI.",
                order=0,
            ),
            dict(
                title="Backend Development",
                description="Database design, authentication, and business logic that scales cleanly.",
                order=1,
            ),
            dict(
                title="API Development",
                description="RESTful APIs and third-party integrations, documented and tested.",
                order=2,
            ),
            dict(
                title="Trading Automation",
                description="Bots and tools that integrate market data APIs and execute logic reliably.",
                order=3,
            ),
            dict(
                title="Database Systems",
                description="Relational schema design, migrations, and query performance tuning.",
                order=4,
            ),
        ]
        for item in services:
            Service.objects.update_or_create(title=item["title"], defaults=item)

        social_links = [
            dict(platform="email", label="Email", url=f"mailto:{profile.email}", order=0),
            dict(platform="github", label="GitHub", url="https://github.com/yourusername", order=1),
            dict(platform="linkedin", label="LinkedIn", url="https://linkedin.com/in/yourusername", order=2),
            dict(platform="telegram", label="Telegram", url="https://t.me/yourusername", order=3),
            dict(platform="whatsapp", label="WhatsApp", url="https://wa.me/2348105737397", order=4),
        ]
        for item in social_links:
            SocialLink.objects.update_or_create(label=item["label"], defaults=item)

        projects = [
            dict(
                title="FFX Market",
                summary="Forex market data and trading dashboard.",
                description=(
                    "A dashboard for tracking forex market data in real time, built to "
                    "feed the trading automation platform. Replace this with your real "
                    "screenshots, description, and links from the admin."
                ),
                tech_stack="Python, Django, PostgreSQL, REST APIs",
                features="Real-time price feed\nHistorical charting\nAlerting on price thresholds",
                year="2026",
                featured=True,
                order=0,
            ),
            dict(
                title="Trading Bot Automation Platform",
                summary="Automated trading bot integrating external market APIs.",
                description=(
                    "An automated trading bot using Python and Django, integrating "
                    "third-party APIs for real-time market data and trade execution, "
                    "with backend architecture for data processing and automation logic."
                ),
                tech_stack="Python, Django, Celery, REST APIs",
                features="Automated trade execution\nReal-time data ingestion\nPerformance and reliability testing",
                year="Ongoing",
                featured=True,
                order=1,
            ),
            dict(
                title="Banking / Asset Management System",
                summary="Backend system for tracking accounts and assets.",
                description=(
                    "Placeholder project — replace with your real banking / asset "
                    "management build: description, tech stack, and screenshots."
                ),
                tech_stack="Django, PostgreSQL, DRF",
                features="Account modelling\nTransaction history\nRole-based access",
                year="2025",
                order=2,
            ),
            dict(
                title="Apartment Booking System",
                summary="Booking platform for short-let apartments.",
                description=(
                    "Placeholder project — replace with your real apartment booking "
                    "build: description, tech stack, and screenshots."
                ),
                tech_stack="Django, PostgreSQL, HTMX",
                features="Availability calendar\nBooking & payments flow\nHost dashboard",
                year="2025",
                order=3,
            ),
            dict(
                title="Restaurant / Cafe Platform",
                summary="Ordering platform for a restaurant or cafe.",
                description=(
                    "Placeholder project — replace with your real restaurant/cafe "
                    "platform build: description, tech stack, and screenshots."
                ),
                tech_stack="Django, React, PostgreSQL",
                features="Menu management\nOnline ordering\nOrder tracking",
                year="2024",
                order=4,
            ),
        ]
        for item in projects:
            Project.objects.update_or_create(title=item["title"], defaults=item)

        self.stdout.write(self.style.SUCCESS("Seed data loaded. Edit everything from /admin/."))
