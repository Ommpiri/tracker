import sys
import os

# Add backend folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app import app

# Export app for Vercel Serverless Function runtime
app = app
