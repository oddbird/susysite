#!/usr/bin/env python
"""
Alternative run-rstblog wrapper script; adds our modules path.

"""
import os, sys

from rstblog.cli import main
from rstblog.modules import add_module_path

HERE = os.path.dirname(os.path.abspath(__file__))
MODULES = os.path.join(HERE, "modules")
LIB = os.path.join(HERE, "lib")

if __name__ == "__main__":
    sys.path.insert(0, LIB)
    add_module_path(MODULES)
    main()