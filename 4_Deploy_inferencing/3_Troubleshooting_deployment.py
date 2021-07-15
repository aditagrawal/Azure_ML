### Check the service state

from azureml.core.webservice import AksWebservice

# Get the deployed service
service = AksWebservice(name='classifier-service', workspace=ws)

# Check its state
print(service.state)

### Review service logs

print(service.get_logs())

### Deployment and runtime errors can be easier to diagnose by deploying the service as a container in a local Docker instance, like this:

from azureml.core.webservice import LocalWebservice

deployment_config = LocalWebservice.deploy_configuration(port=8890)
service = Model.deploy(ws, 'test-svc', [model], inference_config, deployment_config)

print(service.run(input_data = json_data))

# You can then troubleshoot runtime issues by making changes to the scoring file that is referenced in the inference configuration, and reloading the service without redeploying it (something you can only do with a local service):

service.reload()
print(service.run(input_data = json_data))
