from spynnaker.pyNN.utilities import utility_calls
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter
from data_specification.enums.data_type import DataType
from spynnaker.pyNN.models.neuron.threshold_types.abstract_threshold_type \
    import AbstractThresholdType


class MyThresholdType(AbstractThresholdType):
    """ A threshold that is a static value
    """
    def __init__(
            self, n_neurons,

            # TODO: update parameters
            threshold_value, my_threshold_parameter):
        AbstractThresholdType.__init__(self)
        self._n_neurons = n_neurons

        # TODO: Store any parameters
        self._threshold_value = utility_calls.convert_param_to_numpy(
            threshold_value, n_neurons)
        self._my_threshold_parameter = utility_calls.convert_param_to_numpy(
            my_threshold_parameter, n_neurons)

    # TODO: Add getters and setters for the parameters

    @property
    def threshold_value(self):
        return self._threshold_value

    @threshold_value.setter
    def threshold_value(self, threshold_value):
        self._threshold_value = utility_calls.convert_param_to_numpy(
            threshold_value, self._n_neurons)

    @property
    def my_threshold_parameter(self):
        return self._my_threshold_parameter

    @my_threshold_parameter.setter
    def my_threshold_parameter(self, my_threshold_parameter):
        self._my_threshold_parameter = utility_calls.convert_param_to_numpy(
            my_threshold_parameter, self._n_neurons)

    def get_n_threshold_parameters(self):

        # TODO: update to return the number of parameters
        # Note: This must match the number of values in the threshold_type_t
        # data structure in the C code
        return 2

    def get_threshold_parameters(self):

        # TODO: update to the return the parameters
        # Note: The order of the parameters must match the order in the
        # threshold_type_t data structure in the C code
        return [
            NeuronParameter(self._threshold_value, DataType.S1615),
            NeuronParameter(self._my_threshold_parameter, DataType.S1615)
        ]

    def get_n_cpu_cycles_per_neuron(self):

        # TODO: update to the number of cycles used by\
        # threshold_type_is_above_threshold
        # Note: This can be guessed
        return 10
