# main interface to use the spynnaker related tools.
# ALL MODELS MUST INHERIT FROM THIS
from spynnaker.pyNN.models.neuron.abstract_population_vertex \
    import AbstractPopulationVertex


# TODO: additional inputs (import as required)
# There are no standard models for this, so import your own
from python_models.neuron.additional_inputs.my_additional_input \
    import MyAdditionalInput

# TODO: input types (all imported for help, only use one)
from spynnaker.pyNN.models.neuron.input_types.input_type_current \
    import InputTypeCurrent
from spynnaker.pyNN.models.neuron.input_types.input_type_conductance \
    import InputTypeConductance

# TODO: neuron models (all imported for help, only use one)
# standard
from spynnaker.pyNN.models.neuron.neuron_models.\
    neuron_model_leaky_integrate_and_fire \
    import NeuronModelLeakyIntegrateAndFire
from spynnaker.pyNN.models.neuron.neuron_models.neuron_model_leaky_integrate \
    import NeuronModelLeakyIntegrate
from spynnaker.pyNN.models.neuron.neuron_models.neuron_model_izh \
    import NeuronModelIzh

# new model template
from python_models.neuron.neuron_models.my_neuron_model \
    import MyNeuronModel

# TODO: synapse types (all imported for help, only use one)
# standard
from spynnaker.pyNN.models.neuron.synapse_types.synapse_type_exponential \
    import SynapseTypeExponential
from spynnaker.pyNN.models.neuron.synapse_types.synapse_type_dual_exponential \
    import SynapseTypeDualExponential

# new model template
from python_models.neuron.synapse_types.my_synapse_type \
    import MySynapseType


# threshold types (all imported for help, only use one)
# standard
from spynnaker.pyNN.models.neuron.threshold_types.threshold_type_static \
    import ThresholdTypeStatic

# new model template
from python_models.neuron.threshold_types.my_threshold_type\
    import MyThresholdType


class MyModelCurrExp(AbstractPopulationVertex):

    # TODO: Set the maximum number of atoms per core that can be supported.
    # For more complex models, you might need to reduce this number.
    _model_based_max_atoms_per_core = 256

    # TODO: update accordingly
    # default parameters for this build. Used when end user has not entered any
    default_parameters = {
        'v_thresh': -50.0, 'tau_syn_E': 5.0, 'tau_syn_I': 5.0,
        'i_offset': 0, 'my_parameter': -70.0}

    def __init__(
            self, n_neurons, spikes_per_second=None, ring_buffer_sigma=None,
            incoming_spike_buffer_size=None, constraints=None, label=None,

            # TODO: neuron model parameters (add / remove as required)
            # neuron model parameters
            my_parameter=default_parameters['my_parameter'],
            i_offset=default_parameters['i_offset'],

            # TODO: threshold types parameters (add / remove as required)
            # threshold types parameters
            v_thresh=default_parameters['v_thresh'],

            # TODO: synapse type parameters (add /remove as required)
            # synapse type parameters
            tau_syn_E=default_parameters['tau_syn_E'],
            tau_syn_I=default_parameters['tau_syn_I'],

            # TODO: Optionally, you can add initial values for the state
            # variables; this is not technically done in PyNN
            v_init=None):

        # TODO: create your neuron model class (change if required)
        # create your neuron model class
        neuron_model = MyNeuronModel(
            n_neurons, i_offset, my_parameter)

        # TODO: create your synapse type model class (change if required)
        # create your synapse type model
        synapse_type = SynapseTypeExponential(
            n_neurons, tau_syn_E, tau_syn_I)

        # TODO: create your input type model class (change if required)
        # create your input type model
        input_type = InputTypeCurrent()

        # TODO: create your threshold type model class (change if required)
        # create your threshold type model
        threshold_type = ThresholdTypeStatic(n_neurons, v_thresh)

        # TODO: create your own additional inputs (change if required).
        # create your own additional inputs
        additional_input = None

        # instantiate the sPyNNaker system by initialising
        #  the AbstractPopulationVertex
        AbstractPopulationVertex.__init__(

            # standard inputs, do not need to change.
            self, n_neurons=n_neurons, label=label,
            spikes_per_second=spikes_per_second,
            ring_buffer_sigma=ring_buffer_sigma,
            incoming_spike_buffer_size=incoming_spike_buffer_size,

            # TODO: Ensure the correct class is used below
            max_atoms_per_core=MyModelCurrExp._model_based_max_atoms_per_core,

            # These are the various model types
            neuron_model=neuron_model, input_type=input_type,
            synapse_type=synapse_type, threshold_type=threshold_type,
            additional_input=additional_input,

            # TODO: Give the model a name (shown in reports)
            model_name="MyModelCurrExp",

            # TODO: Set this to the matching binary name
            binary="my_model_curr_exp.aplx")

    @staticmethod
    def get_max_atoms_per_core():

        # TODO: Ensure the correct class is used below
        return MyModelCurrExp._model_based_max_atoms_per_core

    @staticmethod
    def set_max_atoms_per_core(new_value):

        # TODO: Ensure the correct class is used below
        MyModelCurrExp._model_based_max_atoms_per_core = new_value
