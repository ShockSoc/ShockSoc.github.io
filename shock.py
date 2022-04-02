from os import path
from shocksoc_app.app import app
from shocksoc_app.freeze import freezer
import os, fnmatch, sys



if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)
