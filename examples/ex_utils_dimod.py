import dimod

import optneal as opn


def ex_bqm():
    bqm = dimod.BinaryQuadraticModel.from_qubo({(0, 1): 1}, 0)
    print(bqm)

    path_json = 'bqm.json'
    opn.save_bqm(path_json, bqm)

    bqm_loaded = opn.load_bqm(path_json)
    print(bqm == bqm_loaded)


def ex_sampleset():
    sampleset = dimod.SampleSet.from_samples([[1, 0, 1], [0, 1, 0], [0, 1, 0]], 'BINARY', 0)
    print(sampleset)

    path_json = 'sampleset.json'
    opn.save_sampleset(path_json, sampleset)

    sampleset_loaded = opn.load_sampleset(path_json)
    print(sampleset == sampleset_loaded)


def main():
    ex_bqm()
    ex_sampleset()


if __name__ == '__main__':
    main()
