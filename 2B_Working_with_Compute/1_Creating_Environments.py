### Creating an environment from a specification file

# For example, you could save the following Conda configuration settings in a file named conda.yml:

name: py_env
dependencies:
  - numpy
  - pandas
  - scikit-learn
  - pip:
    - azureml-defaults

# You could then use the following code to create an Azure Machine Learning environment from the saved specification file

from azureml.core import Environment
env = Environment.from_conda_specification(name='training_environment',
                                           file_path='./conda.yml')

### Creating an environment from an existing Conda environment

# If you have an existing Conda environment defined on your workstation, you can use it to define an Azure Machine Learning environment:

from azureml.core import Environment
env = Environment.from_existing_conda_environment(name='training_environment',
                                                  conda_environment_name='py_env')

### Creating an environment by specifying packages

from azureml.core import Environment
from azureml.core.conda_dependencies import CondaDependencies

env = Environment('training_environment')
deps = CondaDependencies.create(conda_packages=['scikit-learn','pandas','numpy'],
                                pip_packages=['azureml-defaults'])
env.python.conda_dependencies = deps

### Configuring environment containers

# Usually, environments for experiment script are created in containers. The following code configures a script-based experiment to host the env environment created previously in a container

from azureml.core import Experiment, ScriptRunConfig
from azureml.core.runconfig import DockerConfiguration

docker_config = DockerConfiguration(use_docker=True)

script_config = ScriptRunConfig(source_directory='my_folder',
                                script='my_script.py',
                                environment=env,
                                docker_runtime_config=docker_config)

# Azure Machine Learning uses a library of base images for containers, choosing the appropriate base for the compute target you specify (for example, including Cuda support for GPU-based compute). If you have created custom container images and registered them in a container registry, you can override the default base images and use your own by modifying the attributes of the environment's docker property..

env.docker.base_image='my-base-image'
env.docker.base_image_registry='myregistry.azurecr.io/myimage'

# Alternatively, you can have an image created on-demand based on the base image and additional settings in a dockerfile.

env.docker.base_image = None
env.docker.base_dockerfile = './Dockerfile'

# By default, Azure machine Learning handles Python paths and package dependencies. If your image already includes an installation of Python with the dependencies you need, you can override this behavior by setting python.user_managed_dependencies to True and setting an explicit Python path for your installation.

env.python.user_managed_dependencies=True
env.python.interpreter_path = '/opt/miniconda/bin/python'


