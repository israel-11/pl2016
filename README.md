# Live Plot

##Introduction


Nowadays almost every studies requires collecting, processing, and analyzing massive amounts of data using graphs. Graphing, or visualizing, your data is important to any data analysis, and should always occur before the use of model building or statistical tests. 


In this project, the propose is new brand programming language that enables people to visualize and solve almost any common mathematical plots, just by talking to the computer.  The main motivation is under the impression that graphing in any current language is not easy, because the user needs to implements data structure and it will not be able to use any type of variable; so, why not just use your voice? 


The new language will be implemented using python and a python parser. Python has a huge standard library which is will be helpful creating the new program language. Also, has a good quality documentation for standard library. The plot will be using matplotlib, a python 2D plotting library which generate plots, histograms, power spectra, bar charts, etc. The parser that will be used is going to be PLY (Python Lex-Yacc), because of its rich and good documentation. Finally, for the voice recognition we will use Google Speech Recognition API.  
















##Language features 


Some of the basic features the language will provide are: 
Users can plot basic functions on a cartesian plane without typing.
Functions available:
Lineal 
Example:
Y = x 
Y = x +1
Y = 3x -3
Square
Example
Y = x ^2
Y = 2x^2
Square Root
Cubic Root
Absolute Value
Circle
Some Trigonometric
User will be able to specify the domain of the function by saying, for example:
‘from 0 to 5’ , after the function desired.














##Example of the Program
 When the program start, you will be asked to say something.
Lets say: ‘ Plot x square from -50 to 50’.


The output would look like: 
![alt tag](https://qph.ec.quoracdn.net/main-qimg-ca117e2a54324d3867aafa21c612c006?convert_to_webp=true)
Implementation requirements and tools 


Tools/Libraries
Speech Recognition
Matplotlib








###Installing pre-built packages for Speech Recognition:


This is the installation guide for Ubuntu Linux. But this will probably work on other platforms is well. You will need to install a few packages: PyAudio, PortAudio and SpeechRecognition. PyAudio 0.2.9 is required and you may need to compile that manually.




git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
cd pyaudio
sudo python setup.py install
sudo apt-get installl libportaudio-dev
sudo apt-get install python-dev
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo pip3 install SpeechRecognition


###Installing pre-built packages for Matplotlib:
Most platforms : scientific Python distributions
The first option is to use one of the pre-packaged python distributions that already provide matplotlib built-in. The Continuum.io Python distribution (Anaconda or miniconda) and the Enthought distribution (Canopy) are both excellent choices that “just work” out of the box for Windows, OSX and common Linux platforms. Both of these distributions include matplotlib and lots of other useful tools. Another excellent alternative for Windows users is Python (x, y) .


###Linux : using your package manager
If you are on Linux, you might prefer to use your package manager. matplotlib is packaged for almost every major Linux distribution.
Debian / Ubuntu : sudo apt-get install python-matplotlib
Fedora / Redhat : sudo yum install python-matplotlib
###Mac OSX : using pip
If you are on Mac OSX you can probably install matplotlib binaries using the standard Python installation program pip.
###Windows
If you don’t already have Python installed, we recommend using one of the scipy-stack compatible Python distributions such as WinPython, Python(x,y), Enthought Canopy, or Continuum Anaconda, which have matplotlib and many of its dependencies, plus other useful packages, pre installed.
For standard Python installations you will also need to install compatible versions of setuptools, numpy, python-dateutil, pytz, pyparsing, and cyclerin addition to matplotlib.
For Python 3.5 the Visual C++ Redistributable for Visual Studio 2015 needs to be installed. In case Python 2.7 to 3.4 are not installed for all users (not the default), the Microsoft Visual C++ 2008 ( 64 bit or 32 bit for Python 2.7 to 3.2) or Microsoft Visual C++ 2010 ( 64 bit or 32 bit for Python 3.3 and 3.4) redistributable packages need to be installed.
Matplotlib depends on Pillow for reading and saving JPEG, BMP, and TIFF image files. Matplotlib requires MiKTeX and GhostScript for rendering text with LaTeX. FFmpeg, avconv, mencoder, or ImageMagick are required for the animation module.
The following backends should work out of the box: agg, tkagg, ps, pdf and svg. For other backends you may need to install pycairo, PyQt4, PyQt5,PySide, wxPython, PyGTK, Tornado, or GhostScript.
TkAgg is probably the best backend for interactive use from the standard Python shell or IPython. It is enabled as the default backend for the official binaries. GTK3 is not supported on Windows.
The Windows installers (*.exe) and wheels (*.whl) on the PyPI download page do not contain test data or example code. If you want to try the many demos that come in the matplotlib source distribution, download the *.tar.gz file and look in the examples subdirectory. To run the test suite, copy the libmatplotlibtests and libmpl_toolkitstests directories from the source distribution to sys.prefixLibsite-packagesmatplotlib and sys.prefixLibsite-packagesmpl_toolkits respectively, and install nose, mock, Pillow, MiKTeX, GhostScript, ffmpeg, avconv, mencoder, ImageMagick, and Inkscape.
