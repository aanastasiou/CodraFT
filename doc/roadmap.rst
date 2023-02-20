Roadmap
=======

Future milestones
-----------------

CodraFT 2.5
^^^^^^^^^^^

* Run computations in a separate process:

  - Execute a "computing server" in background, in another process
  - Define a communication protocol between this process and
    CodraFT GUI process based on TCP sockets
  - For each computation, send pickled data and computing function
    to the server and wait for the result
  - It will then possible to stop any computation at any time by killing the
    server process and restarting it (eventually after incrementing the
    communication port number)

* Run computations in a separate process (alternative solution):

  - Use an IPython kernel to provide the same features as described above

* Optimize image displaying performance

CodraFT 2.4
^^^^^^^^^^^

* New plugin system (API for third-party extensions):

   - Objective #1: a plugin must be manageable using a single Python script,
     which includes an extension of `ImageProcessor`, `ActionHandler` and
     new file format support
   - Objective #2: plugins must be simply stored in a folder wich defaults
     to the user directory (same folder as ".CodraFT.ini" configuration file)

* Add a macro-command system:

  - New embedded Python editor
  - Scripts using the same API as high-level applicative test scenarios
  - Support for macro recording

* Add an xmlrpc server to allow external applications controlling
  CodraFT main features (open a signal or an image, open a HDF5 file, etc.)

CodraFT 2.3
^^^^^^^^^^^

* Add "Computing parameters" group box to show last result input parameters

* Add "Copy titles to clipboard" feature in "Edit" menu

* Image processing:

  - Add pixel binning operation (binning factors, operation: sum, mean, ...)
  - Add Total variation denoising filter (TV Chambolle)
  - Add Bilateral filter (denoising)
  - Add Wavelet denoising filter
  - Add white Top-Hat denoising filter

  - Add morphological transforms (disk footprint):

    * White Top-Hat
    * Black Top-Hat
    * Erosion
    * Dilation
    * Opening
    * Closing

  - Add Canny filter (edge detection)
  - Add circle Hough transform (circle detection)
  - Add image intensity levels rescaling
  - Add histogram equalization
  - Add adaptative histogram equalization
  - Add blob detection using Determinant of Hessian method

Other ideas for future releases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Add support for multichannel timeseries

* Add a "Preferences" dialog box to setup all configurable parameters

Past milestones
---------------

CodraFT 2.2
^^^^^^^^^^^

* Optimize image visualization performance

* Add default image visualization settings in .INI configuration file

CodraFT 2.1
^^^^^^^^^^^

* "Open in a new window" feature: add support for multiple separate windows,
  thus allowing to visualize for example two images side by side

* New demo mode

* New command line option features (open/browse HDF5 files at startup)

* ROI features:

  - Add an option to extract multiples ROI on either
    one signal/image (current behavior) or one signal/image per ROI
  - Images: create ROI using array masks
  - Images: add support for circular ROI

CodraFT 2.0
^^^^^^^^^^^

* New data processing and visualization features (see below)

* Fully automated high-level processing features for internal testing purpose,
  as well as embedding CodraFT in a third-party software

* Extensive test suite (unit tests and application tests)
  with 90% feature coverage

CodraFT 1.7
^^^^^^^^^^^

* Major redesign

* Python 3.8 is the new reference

* Dropped Python 2 support

CodraFT 1.6
^^^^^^^^^^^

* Last release supporting Python 2
