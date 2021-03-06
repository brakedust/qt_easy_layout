QtGui = None
QtCore = None
Qt = None

class QtImpl:
    QtGui = None
    QtCore = None
    Qt = None

qti = QtImpl()


def use_pyqt():
    import PyQt4.QtCore
    import PyQt4.QtGui

    global QtGui, QtCore, Qt

    QtGui = PyQt4.QtGui
    QtCore = PyQt4.QtCore
    Qt = PyQt4.QtCore.Qt

    qti.QtGui = QtGui
    qti.QtCore = QtCore
    qti.Qt = Qt

def use_pyside():
    import PySide.QtGui
    import PySide.QtCore

    global QtGui, QtCore, Qt

    QtGui = PySide.QtGui
    QtCore = PySide.QtCore
    Qt = PySide.QtCore.Qt

    qti.QtGui = QtGui
    qti.QtCore = QtCore
    qti.Qt = Qt

try:
    #try to use pyqt by default
    use_pyqt()
except:
    #use pyide if that fails
    use_pyside()



