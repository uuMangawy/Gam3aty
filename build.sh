#!/usr/bin/env bash
# Render build script — runs during deploy to install deps, collect static files,
# and migrate the database.
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

cd gam3aty
python manage.py collectstatic --no-input
python manage.py migrate --no-input
