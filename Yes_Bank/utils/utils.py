import os
import pickle
import numpy as np

def save_object(file_path, obj):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as file_obj:
        pickle.dump(obj, file_obj)


def load_object(file_path):
    with open(file_path, "rb") as file_obj:
        return pickle.load(file_obj)


def save_numpy_array_data(file_path, array):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as file_obj:
        np.save(file_obj, array)


def load_numpy_array_data(file_path):
    with open(file_path, "rb") as file_obj:
        return np.load(file_obj)