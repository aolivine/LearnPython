# import sys
# from cx_Freeze import setup, Executable
# import os
#
# os.environ['TCL_LIBRARY'] = "C:\\Users\\Brian\\Anaconda3\\tcl\\tcl8.6"
# os.environ['TK_LIBRARY'] = "C:\\Users\\Brian\\Anaconda3\\tcl\\tk8.6"
#
# include_files =[
#     "C:\\Users\\Brian\\Anaconda3\\DLLs\\tcl86t.dll",
#     "C:\\Users\\Brian\\Anaconda3\\tcl\\tk86t.dll"
# ]
#
# build_exe_options = {"packages":["os","tkinter"],"include_files":include_files}
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"
#
# setup(name='test to exe',
#       version = '0.1',
#       description='test from py file to exe file',
#       executables = [Executable("ximalayaexe.py")]
#       )