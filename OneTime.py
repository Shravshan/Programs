import distutils.dir_util
import ctypes  # An included library with Python install. def Mbox(title, text, style):       Note the styles are as follows:


distutils.dir_util.mkpath(r'C:\Users\Public\PythonFiles\Input\\')
distutils.dir_util.mkpath(r'C:\Users\Public\PythonFiles\Archive\\')
distutils.dir_util.mkpath(r'C:\Users\Public\PythonFiles\Clean\\')
distutils.dir_util.mkpath(r'C:\Users\Public\PythonFiles\Output\\')


import pymsgbox
pymsgbox.alert(r'Folders created in the location C:\Users\Public\PythonFiles\\', 'Success!')
ctypes.windll.user32.MessageBoxA('Success!', r'Folders created in the location C:\Users\Public\PythonFiles\\', 1)

