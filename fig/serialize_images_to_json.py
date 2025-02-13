"""
serialize_images_to_json
~~~~~~~~~~~~~~~~~~~~~~~~

Utility to serialize parts of the training and validation data to JSON, 
for use with Javascript.  """

#### Libraries
# Standard library
import json
import os
import sys

# My library
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "src"))
import mnist_loader

# Third-party libraries
import numpy as np


# Number of training and validation data images to serialize
NTD = 1000
NVD = 100

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()


def make_data_integer(td):
    # This will be slow, due to the loop.  It'd be better if numpy did
    # this directly.  But numpy.rint followed by tolist() doesn't
    # convert to a standard Python int.
    return [int(x) for x in (td * 256).reshape(784).tolist()]


data = {
    "training": [
        {
            "x": [float(x[0]) for x in training_data[j][0].tolist()],
            "y": [float(y[0]) for y in training_data[j][1].tolist()],
        }
        for j in range(NTD)
    ],
    "validation": [
        {
            "x": [float(x[0]) for x in validation_data[j][0].tolist()],
            "y": float(validation_data[j][1]),
        }
        for j in range(NVD)
    ],
}

f = open("data_1000.json", "w")
json.dump(data, f)
f.close()
