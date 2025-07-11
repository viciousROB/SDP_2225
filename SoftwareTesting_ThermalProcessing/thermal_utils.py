import ctypes
import numpy as np

lib = ctypes.CDLL("./thermal_processing.so")
lib.process_thermal.argtypes = [ctypes.POINTER(ctypes.c_uint16), ctypes.c_int, ctypes.c_int]
lib.process_thermal.restype = ctypes.c_int

def process_thermal_image(np_array):
    rows, cols = np_array.shape
    flat = np_array.flatten()
    ptr = flat.ctypes.data_as(ctypes.POINTER(ctypes.c_uint16))
    result = lib.process_thermal(ptr, rows, cols)
    return result
