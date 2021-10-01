from mublib import require as mreq

def testImportPythonModule():
	try:
		module = mreq("os")
		print("ublib: testImportPythonModule passed.")
	except Exception as e:
		print(f"ublib: testImportPythonModule failed! {e}")

def testImportNonModule():
	try:
		module = mreq("gsdfsdfsherfhsdfhsdfhsdfhbsfd")
		print("ublib: testImportNonModule failed!")
	except Exception as e:
		print("ublib: testImportNonModule passed.")

def testImportFromPip():
	try:
		module = mreq("tiny")
		print("ublib: testImportFromPip passed.")
	except Exception as e:
		print(f"ublib: testImportFromPip failed! {e}")

def runAll():
	testImportPythonModule()
	testImportNonModule()
	testImportFromPip()

if __name__ == "__main__":
	runAll()