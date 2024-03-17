#!/usr/bin/python3
"""this is a task to create a tar file using fabric"""

from fabric.api import *
import os
from datetime import datetime


def do_pack():

    local("mkdir -p verions")
    datetimenw = datetime.now().strftime("%Y%m%d%H%M%S")
    result = local(f"tar -czvf verions/web_static_{datetimenw}.tgz web_static", capture=True)
    if result.succeeded:
        return (os.path.abspath(f"/home/eltawil/Alx/AirBnB_clone_v2/verions/web_static_{datetimenw}.tgz"))
    else:
        return (None)
