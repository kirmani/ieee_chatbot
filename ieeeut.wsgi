import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/kirmani.io/ieeeut/public_html')

from app import app as application
