import os
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from django.core.files.storage import default_storage
from django.core.files import File


MEDIA_ROOT = Path("media")


def upload_media():
    for path in MEDIA_ROOT.rglob("*"):
        if not path.is_file():
            continue

        relative_path = path.relative_to(MEDIA_ROOT).as_posix()

        if default_storage.exists(relative_path):
            print(f"Already exists: {relative_path}")
            print(f"URL: {default_storage.url(relative_path)}")
            continue

        with path.open("rb") as file:
            saved_path = default_storage.save(
                relative_path,
                File(file)
            )

        print(f"Uploaded: {saved_path}")
        print(f"URL: {default_storage.url(saved_path)}")


if __name__ == "__main__":
    upload_media()
    print("\nMedia upload complete.")