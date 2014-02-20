#!/usr/bin/env python
#
# The MIT License (MIT)
#
# Copyright (c) <2013-2014> <Colin Duquesnoy>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
"""
A simple example of use.

Load an ui made in QtDesigner and apply the DarkStyleSheet.


Requirements:
    - Python 2 or Python 3
    - PyQt4

.. note.. :: qdarkstyle does not have to be installed to run 
    the example

"""
import sys
from PyQt4 import QtGui, QtCore
from os.path import abspath, dirname
# make the example runnable without the need to install
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))
import qdarkstyle
import example_pyqt_ui as example_ui

print(qdarkstyle.__file__)

def main():
    """
    Application entry point
    """	
    # create the application and the main window
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    
    # setup ui
    ui = example_ui.Ui_MainWindow()
    ui.setupUi(window)
    window.setWindowTitle("QDarkStyle example")

    # tabify dock widgets to show bug #6
    window.tabifyDockWidget(ui.dockWidget1, ui.dockWidget2)

    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))

    # auto quit after 2s when testing on travis-ci
    if "--travis" in sys.argv:
        QtCore.QTimer.singleShot(2000, app.exit)

    # run
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

