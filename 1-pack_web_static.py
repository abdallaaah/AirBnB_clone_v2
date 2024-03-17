#!/usr/bin/python3
"""this is a task to create a tar file using fabric"""

from fabric.api import *
import os
from datetime import datetime


def do_pack():
    """this function to create a tar file"""
    local("mkdir -p versions")
    datetimenw = datetime.now().strftime("%Y%m%d%H%M%S")
    result = local(f"tar -czvf versions/web_static_{datetimenw}.tgz web_static", capture=True)
    if result.succeeded:
        return (os.path.abspath(f"/home/eltawil/Alx/AirBnB_clone_v2/versions/web_static_{datetimenw}.tgz"))
    else:
        return (None)
