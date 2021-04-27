import json

import dimod


def load_bqm(path_json):
    with open(path_json, 'r') as f:
        ser = json.load(f)
    return dimod.BinaryQuadraticModel.from_serializable(ser)


def save_bqm(path_json, bqm):
    with open(path_json, 'w') as f:
        json.dump(bqm.to_serializable(), f)


def load_sampleset(path_json):
    with open(path_json, 'r') as f:
        ser = json.load(f)
    return dimod.SampleSet.from_serializable(ser)


def save_sampleset(path_json, sampleset, aggregate=False):
    if aggregate:
        sampleset = sampleset.aggregate()

    with open(path_json, 'w') as f:
        json.dump(sampleset.to_serializable(), f)
