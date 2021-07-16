### Creating and registering tabular datasets

# After creating the dataset, the code registers it in the workspace with the name csv_table.

from azureml.core import Dataset

blob_ds = ws.get_default_datastore()
csv_paths = [(blob_ds, 'data/files/current_data.csv'),
             (blob_ds, 'data/files/archive/*.csv')]
tab_ds = Dataset.Tabular.from_delimited_files(path=csv_paths)
tab_ds = tab_ds.register(workspace=ws, name='csv_table')

### Creating and registering file datasets

# The dataset in this example includes all .jpg files in the data/files/images path within the default datastore: After creating the dataset, the code registers it in the workspace with the name img_files.

from azureml.core import Dataset

blob_ds = ws.get_default_datastore()
file_ds = Dataset.File.from_files(path=(blob_ds, 'data/files/images/*.jpg'))
file_ds = file_ds.register(workspace=ws, name='img_files')

### Retrieving a registered dataset

import azureml.core
from azureml.core import Workspace, Dataset

# Load the workspace from the saved config file
ws = Workspace.from_config()

# Get a dataset from the workspace datasets collection
ds1 = ws.datasets['csv_table']

# Alternatively Get a dataset by name from the datasets class
ds2 = Dataset.get_by_name(ws, 'img_files')

### Dataset versioning

# Datasets can be versioned, enabling you to track historical versions of datasets that were used in experiments, and reproduce those experiments with data in the same state. You can create a new version of a dataset by registering it with the same name as a previously registered dataset and specifying the create_new_version property:

img_paths = [(blob_ds, 'data/files/images/*.jpg'),
             (blob_ds, 'data/files/images/*.png')]
file_ds = Dataset.File.from_files(path=img_paths)
file_ds = file_ds.register(workspace=ws, name='img_files', create_new_version=True)

# Retrieving a specific dataset version
img_ds = Dataset.get_by_name(workspace=ws, name='img_files', version=2)
