import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

import glob
import sys
import os

# custom imports
from utils.logging import __logger__

IMG_WIDTH = 224
IMG_HEIGHT = 224

MODEL_URL = "https://tfhub.dev/google/imagenet/resnet_v2_50/classification/4"
LABELS = ["Pneumonia", "Normal"]

Logger = __logger__()


class TensorflowImg():
    def __init__(self):

        self.model = self._load_model()

    def __get_model_path(self):
        """
        Obtains the absolute path of the model

        @return - String - absolute path of the model
        """
        model_folder = os.path.join(
            os.path.dirname(__file__), "models", "*.h5")
        model_path = glob.glob(model_folder)[0]

        Logger.info(f"Using file {model_path}")
        return model_path

    def _load_model(self):
        """
        Loads a saved model from a specified path.
        """

        model = tf.keras.models.load_model(self.__get_model_path(), custom_objects={
                                           "KerasLayer": hub.KerasLayer})
        Logger.info(f"Successfully Loaded model")
        return model

    def __decode_img(self, img):
        """
        Decodes a jpeg image

        NOTE: img[0] is the image type, img[1] is the binary itself
        """
        Logger.info("Decoding image {img.name}")

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

    def predict(self, image_file_collection):
        """
        predict the image

        @param image_file_collection : Array[files] - the image to be predicted

        @return - Array[
                    Array[
                        filename : String,
                        image_label_prediction: String,
                        image_percentage: Integer
                    ]
                ] - 2d array collection of the image and percentage
        """
        response_collection = []
        for image_file in image_file_collection:
            
            decoded_img = self.__decode_img(image_file)

            Logger.info("Predicting Image {image_file.name}")

            prediction = self.model.predict(
                np.expand_dims(decoded_img, axis=0))
            response_collection.append(
                [
                    image_file.name,
                    self._get_image_label(prediction),
                    str(max(prediction[0]))
                ]
            )
        return response_collection
