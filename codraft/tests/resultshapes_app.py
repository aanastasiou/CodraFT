# -*- coding: utf-8 -*-
#
# Licensed under the terms of the CECILL License
# (see codraft/__init__.py for details)

"""
Result shapes application test:

  - Create an image with metadata shapes and ROI
  - Further tests to be done manually: check if copy/paste metadata works
"""
import numpy as np

from codraft.app import run
from codraft.core.model.image import create_image
from codraft.tests import data as test_data

SHOW = True  # Show test in GUI-based test launcher


def create_image_with_resultshapes():
    """Create test image with resultshapes"""
    data = test_data.create_2d_gaussian(600, np.uint16, x0=2.0, y0=3.0)
    image = create_image("Test image with metadata", data)
    for mshape in test_data.create_resultshapes():
        mshape.add_to(image)
    return image


def test():
    """Result shapes test"""
    obj1 = test_data.create_test_image1()
    obj2 = create_image_with_resultshapes()
    obj2.roi = np.array([[10, 10, 60, 400]], int)
    run(console=False, objects=(obj1, obj2), size=(1200, 550))


if __name__ == "__main__":
    test()