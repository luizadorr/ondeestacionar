import sys
import os

root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root)

app_dir = os.path.join(root, "app")
sys.path.insert(0, app_dir)

from app.app import app