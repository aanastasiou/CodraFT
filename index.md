![CodraFT - CODRA's Filtering Tool](https://raw.githubusercontent.com/CODRA-Ingenierie-Informatique/CodraFT/master/doc/images/codraft_banner.png)

[![license](https://img.shields.io/pypi/l/codraft.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/codraft.svg)](https://pypi.org/project/codraft/)
[![PyPI status](https://img.shields.io/pypi/status/codraft.svg)](https://github.com/CODRA-Ingenierie-Informatique/CodraFT)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/codraft.svg)](https://pypi.python.org/pypi/codraft/)

CodraFT is [CODRA](https://codra.net/)'s Filtering Tool.

![CodraFT - CODRA's Filtering Tool](https://raw.githubusercontent.com/CODRA-Ingenierie-Informatique/CodraFT/master/doc/images/dark_light_modes.png)

----

CodraFT is a generic signal and image processing software based on Python scientific
libraries (such as NumPy, SciPy or OpenCV) and Qt graphical user interfaces (thanks to
[guidata](https://pypi.python.org/pypi/guidata) and [guiqwt](https://pypi.python.org/pypi/guiqwt) libraries).

CodraFT is available as a **stand-alone** application (see for example our all-in-one Windows installer) or as an **addon to your Python-Qt application** thanks to advanced automation and embedding features.

See [documentation](https://codraft.readthedocs.io/en/latest/) for more details on
the library and [changelog](https://raw.githubusercontent.com/CODRA-Ingenierie-Informatique/CodraFT/master/CHANGELOG.md) for recent history of changes.

### Credits

Copyrights and licensing:

* Copyright © 2022 [CEA](http://www.cea.fr)-[CODRA](https://codra.net/), Pierre Raybaut
* Licensed under the terms of the BSD 3-Clause License or the CeCILL-B License v1

----

## Key features

### Data visualization

| Signal |  Image | Feature                        |
|:------:|:------:|--------------------------------|
|    •   |    •   | Screenshots (save, copy)       |
|    •   | Z-axis | Lin/log scales                 |
|    •   |    •   | Data table editing             |
|    •   |    •   | Statistics on user-defined ROI |
|    •   |    •   | Markers                        |
|        |    •   | Aspect ratio (1:1, custom)     |
|        |    •   | 50+ available colormaps        |
|        |    •   | X/Y raw/averaged profiles      |
|    •   |    •   | User-defined annotations       |

![1D-Peak detection](https://raw.githubusercontent.com/CODRA-Ingenierie-Informatique/CodraFT/master/doc/images/peak_detection.png)

![2D-Peak detection](https://raw.githubusercontent.com/CODRA-Ingenierie-Informatique/CodraFT/master/doc/images/2dpeak_detection.png)

### Data processing

| Signal | Image | Feature                                            |
|:------:|:-----:|----------------------------------------------------|
|    •   |   •   | Multiple ROI support                               |
|    •   |   •   | Sum, average, difference, product, ...             |
|    •   |   •   | ROI extraction, Swap X/Y axes                      |
|    •   |       | Semi-automatic multi-peak detection                |
|        |   •   | Rotation (flip, rotate), resize, ...               |
|        |   •   | Flat-field correction                              |
|    •   |       | Normalize, derivative, integral                    |
|    •   |   •   | Linear calibration                                 |
|        |   •   | Thresholding, clipping                             |
|    •   |   •   | Gaussian filter, Wiener filter                     |
|    •   |   •   | Moving average, moving median                      |
|    •   |   •   | FFT, inverse FFT                                   |
|    •   |       | Interactive fit: Gauss, Lorenzt, Voigt, polynomial |
|    •   |       | Interactive multigaussian fit                      |
|    •   |   •   | Computing on custom ROI                            |
|    •   |       | FWHM, FW @ 1/e²                                    |
|        |   •   | Centroid (robust method w/r noise)                 |
|        |   •   | Minimum enclosing circle center                    |
|        |   •   | Automatic 2D-peak detection                        |
|        |   •   | Automatic contour extraction (circle/ellipse fit)  |

![Contour detection](https://raw.githubusercontent.com/CODRA-Ingenierie-Informatique/CodraFT/master/doc/images/contour_detection.png)

![Multi-gaussian fit](https://raw.githubusercontent.com/CODRA-Ingenierie-Informatique/CodraFT/master/doc/images/multi_gaussian_fit.png)
