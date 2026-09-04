import sys
import os

# Add current api folder to Python path so `app` package is found directly inside api/
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Fallback path for local development
backend_dir = os.path.join(current_dir, '..', 'backend')
if os.path.exists(backend_dir) and backend_dir not in sys.path:
    sys.path.append(backend_dir)

from app.main import app

# Export app for Vercel Serverless Function runtime
app = app
