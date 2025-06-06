import sys
import os

# Add the correct project root directory to PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# print("Updated PYTHONPATH:", sys.path)

import numpy as np
from random_allocation.comparisons.definitions import *
from random_allocation.comparisons.experiments import run_experiment, PlotType

# Configuration
SAVE_DATA = True  # Set to True to save data to CSV files
SAVE_PLOTS = True  # Set to True to save plots to files, False to display them interactively

# First experiment
params_dict_1 = {'x_var': SIGMA,
                 'y_var': EPSILON,
                 SIGMA: np.exp(np.linspace(np.log(0.2), np.log(5), 20)),
                 DELTA: 1e-10,
                 NUM_STEPS: 100_000,
                 NUM_SELECTED: 1,
                 NUM_EPOCHS: 1}

config_dict_1 = {DISCRETIZATION: 1e-4,
                 MIN_ALPHA: 2,
                 MAX_ALPHA: 60,
                 EPSILON_TOLERANCE: 1e-3,
                 DELTA_TOLERANCE: 1e-10,}

methods_list_1 = [LOCAL, SHUFFLE, POISSON_PLD, ALLOCATION_RDP, ALLOCATION_ANALYTIC, ALLOCATION_DECOMPOSITION]

visualization_config_1 = {'log_x_axis': True, 'log_y_axis': True}

data_1 = run_experiment(params_dict_1, config_dict_1, methods_list_1, visualization_config_1, 'epsilon_vs_sigma', 
                        PlotType.COMBINED, SAVE_DATA, SAVE_PLOTS)

# Second experiment
params_dict_2 = {'x_var': NUM_EPOCHS,
                 'y_var': EPSILON,
                 SIGMA: 1,
                 DELTA: 1e-8,
                 NUM_STEPS: 10_000,
                 NUM_SELECTED: 1,
                 NUM_EPOCHS: np.exp(np.linspace(np.log(1), np.log(1001), 10)).astype(int)}

config_dict_2 = {DISCRETIZATION: 1e-4,
                 MIN_ALPHA: 2,
                 MAX_ALPHA: 60,
                 EPSILON_TOLERANCE: 1e-3,
                 DELTA_TOLERANCE: 1e-10,}

methods_list_2 = [POISSON_RDP, ALLOCATION_RDP, POISSON_PLD]

visualization_config_2 = {'log_x_axis': True, 'log_y_axis': False, 'format_x': lambda x, _: x}
data_2 = run_experiment(params_dict_2, config_dict_2, methods_list_2, visualization_config_2, 'epsilon_vs_epochs', 
                        PlotType.COMPARISON, SAVE_DATA, SAVE_PLOTS)

# Third experiment
params_dict_3 = {'x_var': NUM_STEPS,
                 'y_var': DELTA,
                 SIGMA: 0.3,
                 EPSILON: 10,
                 NUM_STEPS: np.arange(25, 551, 50),
                 NUM_SELECTED: 1,
                 NUM_EPOCHS: 1}

config_dict_3 = {DISCRETIZATION: 1e-4,
                 NUM_EXP: 1_000_000,
                 MIN_ALPHA: 2,
                 MAX_ALPHA: 60,
                 EPSILON_TOLERANCE: 1e-3,
                 DELTA_TOLERANCE: 1e-10,}

methods_list_3 = [POISSON_RDP, ALLOCATION_RDP, POISSON_PLD]

visualization_config_3 = {'log_x_axis': False, 'log_y_axis': True, 'format_x': lambda x, _: int(x)}

data_3 = run_experiment(params_dict_3, config_dict_3, methods_list_3, visualization_config_3, 'delta_vs_steps', 
                        PlotType.COMPARISON, SAVE_DATA, SAVE_PLOTS)

# Fourth experiment
params_dict_4 = {'x_var': NUM_SELECTED,
                 'y_var': EPSILON,
                 SIGMA: 1,
                 DELTA: 1e-6,
                 NUM_STEPS: 2**10,
                 NUM_SELECTED: 2**np.arange(0, 10),
                 NUM_EPOCHS: 1,}

config_dict_4 = {DISCRETIZATION: 1e-4,
                 MIN_ALPHA: 2,
                 MAX_ALPHA: 60,
                 EPSILON_TOLERANCE: 1e-3,
                 DELTA_TOLERANCE: 1e-10,}

methods_list_4 = [POISSON_RDP, ALLOCATION_RDP, ALLOCATION_RDP_DCO]

visualization_config_4 = {'log_x_axis': True, 'log_y_axis': True, 'format_x': lambda x, _: x}
data_4 = run_experiment(params_dict_4, config_dict_4, methods_list_4, visualization_config_4, 
                        'epsilon_vs_selected', PlotType.COMPARISON, SAVE_DATA, SAVE_PLOTS)