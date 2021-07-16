### Running a Script as an Experiment

# An experiment script - To access the experiment run context (which is needed to log metrics) the script must import the azureml.core.Run class and call its get_context method. The script can then use the run context to log metrics, upload files, and complete the experiment, as shown in the following example:

from azureml.core import Run
import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the experiment run context
run = Run.get_context()

# load the diabetes dataset
data = pd.read_csv('data.csv')

# Count the rows and log the result
row_count = (len(data))
run.log('observations', row_count)

# Save a sample of the data
os.makedirs('outputs', exist_ok=True)
data.sample(100).to_csv("outputs/sample.csv", index=False, header=True)

# Complete the run
run.complete()

### To run a script as an experiment -

# Submit the experiment- to run a script as an experiment, you must define a script configuration that defines the script to be run and the Python environment in which to run it. This is implemented by using a ScriptRunConfig object. For example, the following code could be used to run an experiment based on a script in the experiment_files folder (which must also contain any files used by the script, such as the data.csv file in previous script code example):

from azureml.core import Experiment, ScriptRunConfig

# Create a script config
script_config = ScriptRunConfig(source_directory=experiment_folder,
                                script='experiment.py') 

experiment = Experiment(workspace = ws, name = 'my-experiment')
run = experiment.submit(config=script_config)
run.wait_for_completion(show_output=True)

