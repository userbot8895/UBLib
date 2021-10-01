from logging import getLogger
from subprocess import check_call
import sys
import importlib

log = getLogger(__name__)
PY_EXEC = sys.executable if not " " in sys.executable else '"' + sys.executable + '"'

def require(dep):
    while True:
        try:
            m = importlib.import_module(dep)
            return m
        except:
            log.info(f"ublib: Installing {dep}...")
            try:
                # try to install the required package
                check_call([PY_EXEC, "-m", "pip", "install", dep])
                # then try to import the package again if non-zero exit status returned
            except Exception as e:
                # whole module will not be executed and not loaded
                # if required package is not available at pip
                #
                # Module loader will handle this exception
                raise ImportError(f"ublib: Failed to install {dep}: {e}")