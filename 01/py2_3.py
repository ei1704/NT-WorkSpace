import sys
def py2_or_py3():
  major = sys.version_info.major
  if major < 3:
    return 'Python 2'
  else:
    return 'Python 3'

#py2_or_py3()
print(py2_or_py3())