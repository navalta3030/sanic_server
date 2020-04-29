import sys
from os.path import dirname, abspath, join

parent_file = dirname(dirname(abspath(__file__)))
sys.path.append(parent_file)


import tensorflow as tf
import unittest
from helpers import L
from ml_modules.tensorflow_img import TensorflowImg

ml = TensorflowImg()
file_name = join( dirname(abspath(__file__)), "pneumonia.jpg")

class TestML(unittest.TestCase):
  def test_predict(self):
    image = tf.io.read_file(file_name)

    image_collection = L(0, image)
    image_collection.name = "pneumonia.jpg"

    prediction = ml.predict([image_collection])
    self.assertTrue(
      prediction[0][1],
      "Pneumonia"
    )


if __name__ == "__main__":
    unittest.main()