![CodraFT - CODRA's Filtering Tool](https://raw.githubusercontent.com/CODRA-Software/CodraFT/master/doc/images/codraft_banner.png)

[![license](https://img.shields.io/pypi/l/codraft.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/codraft.svg)](https://pypi.org/project/codraft/)
[![PyPI status](https://img.shields.io/pypi/status/codraft.svg)](https://github.com/CODRA-Software/CodraFT)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/codraft.svg)](https://pypi.python.org/pypi/codraft/)

CodraFT is [CODRA](https://codra.net/)'s Filtering Tool.

![CodraFT - CODRA's Filtering Tool](https://raw.githubusercontent.com/CODRA-Software/CodraFT/master/doc/images/dark_light_modes.png)

----

## Overview

CodraFT is a generic signal and image processing software based on Python scientific
libraries (such as NumPy, SciPy or OpenCV) and Qt graphical user interfaces (thanks to
[guidata](https://pypi.python.org/pypi/guidata) and [guiqwt](https://pypi.python.org/pypi/guiqwt) libraries).

----

## Key features

### Data visualization

|                                       | Signal | Image      |
|---------------------------------------|--------|------------|
| Lin/log scales                        | •      | • (Z-axis) |
| Data table editing                    | •      | •          |
| Statistics on user-defined ROI        | •      | •          |
| Markers                               | •      | •          |
| Aspect ratio (1:1, custom)            |        | •          |
| 50+ colormaps                         |        | •          |
| Screenshots (save, copy)              | •      | •          |
| X/Y cross-sections                    |        | •          |
| Averaged X/Y cross-sections           |        | •          |
| Export cross-sections to signal panel |        | •          |

![CodraFT - CODRA's Filtering Tool](https://raw.githubusercontent.com/CODRA-Software/CodraFT/master/doc/images/panorama.png)

### Operations

|                                        | Signal | Image |
|----------------------------------------|--------|-------|
| Sum, average, difference, product, ... | •      | •     |
| ROI extraction, Swap X/Y axes          | •      | •     |
| Peak detection                         | •      |       |
| Rotation (flip, rotate), resize, ...   |        | •     |
| Flat-field correction                  |        | •     |

![CodraFT - CODRA's Filtering Tool](https://raw.githubusercontent.com/CODRA-Software/CodraFT/master/doc/images/peak_detection.png)

### Processing

|                                        | Signal | Image |
|----------------------------------------|--------|-------|
| Normalize, derivative, integral        | •      |       |
| Linear calibration                     | •      | •     |
| Thresholding, clipping                 |        | •     |
| Gaussian filter, Wiener filter         | •      | •     |
| Moving average, moving median          | •      | •     |
| FFT, inverse FFT                       | •      | •     |
| Fit: Gauss, Lorenzt, Voigt, polynomial | •      |       |
| Multigaussian fit                      | •      |       |

## Computing

|                                    | Signal | Image |
|------------------------------------|--------|-------|
| Computing on custom ROI            | •      | •     |
| FWHM, FW @ 1/e²                    | •      |       |
| Centroid (robust method w/r noise) |        | •     |
| Minimum enclosing circle center    |        | •     |

----

See [documentation](https://codraft.readthedocs.io/en/latest/) for more details on
the library and [changelog](CHANGELOG.md) for recent history of changes.

Copyrights and licensing:

* Copyright © 2018 [CEA](http://www.cea.fr)-[CODRA](https://codra.net/), Pierre Raybaut
* Licensed under the terms of the CECILL License. See ``Licence_CeCILL_V2.1-en.txt``.

----

## Installation

### From the installer

CodraFT is available as a stand-alone application, which does not require any Python
distribution to be installed. Just run the installer and you're good to go!

The installer package is available in the [Releases](https://github.com/CODRA-Software/CodraFT/releases) section.

### From the source package

```bash
python setup.py install
```

----

## Dependencies

### Requirements

* Python 3.7+ (reference is Python 3.8)
* [PyQt5](https://pypi.python.org/pypi/PyQt5) 5.15+ (Python Qt bindings)
* [guidata](https://pypi.python.org/pypi/guidata) 2.0+ (set of tools for automatic GUI generation)
* [guiqwt](https://pypi.python.org/pypi/guiqwt) 4.0+ (set of tools for curve and image plotting based on guidata)

### Other optional modules

* [OpenCV](https://pypi.org/project/opencv-python/) for some image processing features
