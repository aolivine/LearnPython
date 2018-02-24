import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Brian\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Brian\\Anaconda3\\tcl\\tk8.6"

include_files =[
    "C:\\Users\\Brian\\Anaconda3\\DLLs\\tcl86t.dll",
    "C:\\Users\\Brian\\Anaconda3\\tcl\\tk86t.dll"
]
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","tkinter"], "include_files":include_files}
# options = {
#     'build_exe': {
#         'includes': [
#             'testfreeze_1',
#             'testfreeze_2'
#         ],
#         'path': sys.path + ['modules']
#     }
# }
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable('SimpleTkApp.py', base=base)
]
setup(  name = "guifoo",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = executables)


# python setup.py build
# python setup.py bdist_msi
# python setup.py bdist_dmg