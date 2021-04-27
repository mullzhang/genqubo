import networkx as nx
import dimod

from optneal.dimod_generators_random import normal
from optneal import LeapHybridDQMSampler


def main():
    K_7 = nx.complete_graph(7)
    bqm = normal(K_7, dimod.SPIN, loc=0.0, scale=1.0, zero_lbias=True)
    print(bqm)

    token = 'YOUR_DWAVE_SAPI_TOKEN'
    solver = 'hybrid_discrete_quadratic_model_version1'
    endpoint = 'https://cloud.dwavesys.com/sapi/'
    sampler = LeapHybridDQMSampler(token=token, solver=solver, endpoint=endpoint)

    # This sampler is acceptable for binary quadratic model(BQM).
    sampleset = sampler.sample(bqm)
    print(sampleset)


if __name__ == '__main__':
    main()
