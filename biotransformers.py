from sklearn.preprocessing import FunctionTransformer
import numpy as np

def get_log_transformer():
    log_transformer = FunctionTransformer(np.log1p, validate=True)
    return log_transformer