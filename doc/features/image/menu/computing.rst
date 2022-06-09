"Computing" menu
================

.. image:: /images/shots/i_computing.png

Regions of interest
    Open a dialog box to setup multiple Region Of Interests (ROI).
    ROI are stored as metadata, and thus attached to image.

    ROI definition dialog is exactly the same as ROI extraction (see above).

    .. figure:: /images/shots/i_roi_image.png

        An image with ROI.

Statistics
    Compute statistics on selected image and show a summary table.

    .. figure:: /images/shots/i_stats.png

        Example of statistical summary table: each row is associated to an ROI
        (the first row gives the statistics for the whole data).

Centroid
    Compute image centroid using a Fourier transform method
    (as discussed by `Weisshaar et al. <http://www.mnd-umwelttechnik.fh-wiesbaden.de/pig/weisshaar_u5.pdf>`_).
    This method is quite insensitive to background noise.

Minimum enclosing circle center
    Compute the circle contour enclosing image values above
    a threshold level defined as the half-maximum value.

    .. warning::
        This feature requires `OpenCV for Python <https://pypi.org/project/opencv-python/>`_.

2D peak detection
    Automatically find peaks on image using a minimum-maximum filter algorithm.

    .. figure:: /images/shots/i_peak2d_test.png

        Example of 2D peak detection.

Contour detection
    Automatically extract contours and fit them using a circle or an ellipse.

    .. figure:: /images/shots/i_contour_test.png

        Example of contour detection.

.. note:: Computed scalar results are systematically stored as metadata.
    Metadata is attached to image and serialized with it when exporting
    current session in a HDF5 file.