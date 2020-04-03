import tensorflow as tf
import glob

# custom imports
from logging import __logger__

class TensorflowImg():
  def __init__(self):
    self.logger = __logger__()

  def __get_model_path(self):
    """
    Obtains the absolute path of the model

    @return - String - absolute path of the model
    """

    model_folder = os.path.join(Path(__file__), "models", "*.h5")
    model_path = glob.glob(model_folder)
    return model_path

  def __load_model(self):
    """
    Loads a saved model from a specified path.
    """

    model = tf.keras.models.load_model(self.__get_model_path(), custom_objects={"KerasLayer":hub.KerasLayer})
    return model