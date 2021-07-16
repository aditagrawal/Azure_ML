### 1. Creating a workspace

from azureml.core import Workspace
    
ws = Workspace.create(name='aml-workspace', 
                subscription_id='123456-abc-123...',
                resource_group='aml-resources',
                create_resource_group=True,
                location='eastus'
                 )

# or Use the Azure Command Line Interface (CLI) with the Azure Machine Learning CLI extension. For example, you could use the following command (which assumes a resource group named aml-resources has already been created)-

az ml workspace create -w 'aml-workspace' -g 'aml-resources'

### 2. Connecting to a workspace

# The easiest way to connect to a workspace is to use a workspace configuration file, which includes the Azure subscription, resource group, and workspace details as shown here:
#JSON

{
    "subscription_id": "1234567-abcde-890-fgh...",
    "resource_group": "aml-resources",
    "workspace_name": "aml-workspace"
}

# To connect to the workspace using the configuration file, you can use the from_config method of the Workspace class in the SDK, as shown here:
# By default, the from_config method looks for a file named config.json in the folder containing the Python code file, but you can specify another path if necessary.

from azureml.core import Workspace
ws = Workspace.from_config()

# Alternatively

from azureml.core import Workspace
ws = Workspace.get(name='aml-workspace',
                   subscription_id='1234567-abcde-890-fgh...',
                   resource_group='aml-resources')


### 3. Working with Worspaces
# The Workspace class is the starting point for most code operations. For example, you can use its compute_targets attribute to retrieve a dictionary object containing the compute targets defined in the workspace, like this:

for compute_name in ws.compute_targets:
    compute = ws.compute_targets[compute_name]
    print(compute.name, ":", compute.type)
    
    
### The Azure Machine Learning CLI Extension
# The Azure command-line interface (CLI) is a cross-platform command-line tool for managing Azure resources. The Azure Machine Learning CLI extension is an additional package that provides commands for working with Azure Machine Learning. 
# After installing the Azure CLI, you can add the Azure Machine Learning CLI extension by running the following command:

az extension add -n azure-cli-ml

# To use the Azure Machine Learning CLI extension, run the az ml command with the appropriate parameters for the action you want to perform. For example, to list the compute targets in a workspace, run the following command:

az ml computetarget list -g 'aml-resources' -w 'aml-workspace'

