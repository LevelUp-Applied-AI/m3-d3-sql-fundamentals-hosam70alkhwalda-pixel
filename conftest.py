import os
import sys

ROOT = os.path.dirname(os.path.abspath(_file_))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)