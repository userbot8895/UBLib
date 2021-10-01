Q='"'
from logging import getLogger as B
from subprocess import check_call as C
import sys as A,importlib as D
E=B(__name__)
F=A.executable if not' 'in A.executable else Q+A.executable+Q
def H(dep):
	A=dep
	while True:
		try:B=D.import_module(A);return B
		except:
			E.info(f"ublib: Installing {A}...")
			try:C([F,'-m','pip','install',A])
			except Exception as G:raise ImportError(f"ublib: Failed to install {A}: {G}")