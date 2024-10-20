# __init__.py
from .story_integration import register_ip_asset
from .main import app

print("Your Project Package has been imported!")

__all__ = ['register_ip_asset', 'app']

