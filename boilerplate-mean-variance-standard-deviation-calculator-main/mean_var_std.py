import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    # using reshape() to covert this array in desired array.
    calculations = np.array(list).reshape(3,3)

    dict = {
        'mean':[calculations.mean(0).tolist(),calculations.mean(1).tolist(),calculations.mean()],
        'variance':[calculations.var(0).tolist(),calculations.var(1).tolist(),calculations.var()],
        'standard deviation':[calculations.std(0).tolist(),calculations.std(1).tolist(),calculations.std()],
        'max':[calculations.max(0).tolist(),calculations.max(1).tolist(),calculations.max()],
        'min':[calculations.min(0).tolist(),calculations.min(1).tolist(),calculations.min()],
        'sum':[calculations.sum(0).tolist(),calculations.sum(1).tolist(),calculations.sum()]
    } 

    return dict