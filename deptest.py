from ublib import dependencies as d

def testImportPythonModule():
	try:
		module = d.require("os")
		print("ublib: testImportPythonModule passed.")
	except Exception as e:
		print(f"ublib: testImportPythonModule failed! {e}")

def testImportNonModule():
	try:
		module = d.require("gsdfsdfsherfhsdfhsdfhsdfhbsfd")
		print("ublib: testImportNonModule failed!")
	except Exception as e:
		print("ublib: testImportNonModule passed.")

def testImportFromPip():
	try:
		module = d.require("tiny")
		print("ublib: testImportFromPip passed.")
	except Exception as e:
		print(f"ublib: testImportFromPip failed! {e}")

def runAll():
	testImportPythonModule()
	testImportNonModule()
	testImportFromPip()

if __name__ == "__main__":
	runAll()