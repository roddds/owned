# -*- coding: utf-8 -*-
import os
import sys
from unipath import Path
from datetime import datetime

PROJECT_DIR = Path(__file__).parent.parent

sys.path.append(PROJECT_DIR.child('apps'))
sys.path.append(PROJECT_DIR.child('libs'))
