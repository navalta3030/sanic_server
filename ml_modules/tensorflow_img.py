import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

import glob
import sys
import os

# custom imports
from utils.logging import __logger__

IMG_WIDTH = 128
IMG_HEIGHT = 128

MODEL_URL = "https://tfhub.dev/google/imagenet/resnet_v2_50/classification/4"
LABELS = ["EFFUSION", "NORMAL"]


class TensorflowImg():
    def __init__(self):
        self.logger = __logger__()
        # self.model = self.__load_model()
        self.model = "No model for now"

    def __get_model_path(self):
        """
        Obtains the absolute path of the model

        @return - String - absolute path of the model
        """
        model_folder = os.path.join(
            os.path.dirname(__file__), "models", "*.h5")
        model_path = glob.glob(model_folder)[0]
        return model_path

    def __load_model(self):
        """
        Loads a saved model from a specified path.
        """

        model = tf.keras.models.load_model(self.__get_model_path(), custom_objects={
                                           "KerasLayer": hub.KerasLayer})
        return model

    def __decode_img(self, img):
        """
        Decodes a jpeg image

        NOTE: img[0] is the image type, img[1] is the binary itself
        """

        # convert the compressed string to a 3D uint8 tensor
        img = tf.image.decode_jpeg(img[1], channels=3)
        # Use `convert_image_dtype` to convert to floats in the [0,1] range.
        img = tf.image.convert_image_dtype(img, tf.float32)
        # resize the image to the desired size.
        return tf.image.resize(img, [IMG_WIDTH, IMG_HEIGHT])

    def _get_image_label(self, prediction):
        """
        Takes an image file path name and the associated label,
        processes the image and returns a tuple of (image, label).
        """
        return LABELS[np.argmax(prediction)]

    def predict(self, image):
        """
        predict the image

        @param image : file/base64? - the image to be predicted

        @return - Array[ Array[String, percent] ] - 2d array collection of the image and percentage
        """
        decoded_img = self.__decode_img(image)
        prediction = self.model.predict(np.expand_dims(decoded_img, axis=0))
        return self._get_image_label(prediction)
