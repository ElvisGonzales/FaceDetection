# -*- coding: utf-8 -*-
"""Flower_Classification_with_TFLite_Model_Maker (Beta).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sqBewUnvdATOO-yblj55EBFb2sM24XHR

##### Copyright 2020 The TensorFlow Authors.
"""

#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""# Flower classification with TensorFlow Lite Model Maker with TensorFlow 2.0

<table class="tfo-notebook-buttons" align="left">
  <td>
    <a target="_blank" href="https://colab.research.google.com/github/tensorflow/examples/blob/master/lite/codelabs/flower_classification/ml/Flower_Classification_with_TFLite_Model_Maker.ipynb">      
    <img src="https://www.tensorflow.org/images/colab_logo_32px.png" />
    Run in Google Colab</a>
  </td>
  <td>
    <a target="_blank" href="https://github.com/tensorflow/examples/blob/master/lite/codelabs/flower_classification/ml/Flower_Classification_with_TFLite_Model_Maker.ipynb">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub</a>
  </td>
</table>

Model Maker library simplifies the process of adapting and converting a TensorFlow neural-network model to particular input data when deploying this model for on-device ML applications.

This notebook shows an end-to-end example that utilizes this Model Maker library to illustrate the adaption and conversion of a commonly-used image classification model to classify flowers on a mobile device.

## Prerequisites

To run this example, we first need to make a copy of this notebook. Click on "Copy to Drive" at the top of this notebook. Then we need to install serveral required packages, including Model Maker package that in github [repo](https://github.com/tensorflow/examples/tree/master/tensorflow_examples/lite/model_maker).
"""

!pip install -q tflite-model-maker

"""Import the required packages."""

from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader

import tensorflow as tf
assert tf.__version__.startswith('2')

import matplotlib.pyplot as plt
import numpy as np

"""## Simple End-to-End Example

### Get the data path

Let's get some images to play with this simple end-to-end example. Hundreds of images is a good start for Model Maker while more data could achieve better accuracy.
"""

image_path = tf.keras.utils.get_file(
      '/content/drive/MyDrive/banderas',
      'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',
      untar=True)

"""You could replace `image_path` with your own image folders. As for uploading data to colab, you could find the upload button in the left sidebar shown in the image below with the red rectangle. Just have a try to upload a zip file and unzip it. The root file path is the current path.

<img src="https://storage.googleapis.com/download.tensorflow.org/models/tflite/screenshots/model_maker_image_classification.png" alt="Upload File" width="800" hspace="100">

If you prefer not to upload your images to the cloud, you could try to run the library locally following the [guide](https://github.com/tensorflow/examples/tree/master/tensorflow_examples/lite/model_maker) in github.

### Run the example
The example just consists of 4 lines of code as shown below, each of which representing one step of the overall process.

1.   Load input data specific to an on-device ML app. Split it to training data and testing data.
"""

data = DataLoader.from_folder(image_path)
train_data, test_data = data.split(0.9)

"""2. Customize the TensorFlow model."""

model = image_classifier.create(train_data)

"""3. Evaluate the model."""

loss, accuracy = model.evaluate(test_data)

"""4.  Export to TensorFlow Lite model.
You could download it in the left sidebar same as the uploading part for your own use.
"""

model.export(export_dir='.')

"""5. Download the trained model by clicking on the folder icon on the left hand side. Right-click on "model.tflite" and select download. Or run the following code:"""

from google.colab import files
files.download('model.tflite')

"""After this simple 5 steps, we can now continue to the next step in the [codelab](https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android-beta/#2).

For a more comprehensive guide to TFLite Model Maker, please refer to this [notebook](https://colab.sandbox.google.com/github/tensorflow/examples/blob/master/tensorflow_examples/lite/model_maker/demo/image_classification.ipynb) and its [documentation](https://github.com/tensorflow/examples/tree/master/tensorflow_examples/lite/model_maker).
"""