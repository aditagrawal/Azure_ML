### 1. Setting the Experiment Run Context

from azureml.core import Experiment

# create an experiment variable
experiment = Experiment(workspace = ws, name = "my-experiment")

# start the experiment
run = experiment.start_logging()

# experiment code goes here

# end the experiment
run.complete()

### 2. Logging Metrics and Creating Outputs

# Logging Metrics
# log: Record a single named value.
# log_list: Record a named list of values.
# log_row: Record a row with multiple columns.
# log_table: Record a dictionary as a table.
# log_image: Record an image file or a plot.

from azureml.core import Experiment
import pandas as pd

# Create an Azure ML experiment in your workspace
experiment = Experiment(workspace = ws, name = 'my-experiment')

# Start logging data from the experiment
run = experiment.start_logging()

# load the dataset and count the rows
data = pd.read_csv('data.csv')
row_count = (len(data))

# Log the row count
run.log('observations', row_count)

# Complete the experiment
run.complete()

### 3. Retrieving and Viewing Logged Metrics

from azureml.widgets import RunDetails
RunDetails(run).show()

### 4. Experiment output files
# In addition to logging metrics, an experiment can generate output files. Often these are trained machine learning models, but you can save any sort of file and make it available as an output of your experiment run. The output files of an experiment are saved in its outputs folder.

run.upload_file(name='outputs/sample.csv', path_or_stream='./sample.csv')

### 5. Retrieve experiment output files

import json
files = run.get_file_names()
print(json.dumps(files, indent=2))


