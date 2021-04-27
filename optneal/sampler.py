import dimod
from dwave.system import LeapHybridDQMSampler as _LeapHybridDQMSampler


def bqm_to_dqm(bqm):
    """Change bqm to dqm."""
    dqm = dimod.DiscreteQuadraticModel()
    for i in bqm.variables:
        dqm.add_variable(2, label=i)
    for i, v in bqm.linear.items():
        dqm.set_linear(i, [0, v])
    for (i, j), v in bqm.quadratic.items():
        dqm.set_quadratic(i, j, {(1, 1): v})
    return dqm


class LeapHybridDQMSampler(_LeapHybridDQMSampler, dimod.Sampler):
    """A class for using Leap's cloud-based hybrid DQM solvers
       acceptable for binary quadratic models (BQM)."""

    def sample(self, bqm, time_limit=None,
               compress=False, compressed=None, **kwargs):
        """Sample from the specified binary quadratic model.

        Args:
            bqm (:obj:`dimod.BinaryQuadraticModel`):
                Binary quadratic model.

            time_limit (int, optional):
                Maximum run time, in seconds, to allow the solver to work on the
                problem. Must be at least the minimum required for the number of
                problem variables, which is calculated and set by default.

                :meth:`~dwave.system.samplers.LeapHybridDQMSampler.min_time_limit`
                calculates (and describes) the minimum time for your problem.

            compress (binary, optional):
                Compresses the DQM data when set to True. Use if your problem
                somewhat exceeds the maximum allowed size. Compression tends to
                be slow and more effective on homogenous data, which in this
                case means it is more likely to help on DQMs with many identical
                integer-valued biases than ones with random float-valued biases,
                for example.

            compressed (binary, optional):
                Deprecated; please use ``compress`` instead.

            **kwargs:
                Optional keyword arguments for the solver, specified in
                :attr:`~dwave.system.samplers.LeapHybridDQMSampler.parameters`.

        Returns:
            :class:`dimod.SampleSet`: A sample set.

    Examples:
        See the example in :class:`LeapHybridDQMSampler`.

        """
        dqm = bqm_to_dqm(bqm)
        sampleset_disc = self.sample_dqm(
            dqm, time_limit, compress, compressed, **kwargs
        )

        # change vartype
        sampleset = dimod.SampleSet.from_samples(
            sampleset_disc.record.sample, bqm.vartype, sampleset_disc.record.energy,
            sampleset_disc.info, sampleset_disc.record.num_occurrences
        )
        return sampleset
