@echo off
rem Double-click launcher for the seed_nav sidebar (Windows).
cd /d "%~dp0"
start "" pythonw APPS\seed_nav\seed_nav.py || start "" python APPS\seed_nav\seed_nav.py
