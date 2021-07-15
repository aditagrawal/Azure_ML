### 1. Configure an automated machine learning experiment

from azureml.train.automl import AutoMLConfig

automl_run_config = RunConfiguration(framework='python')
automl_config = AutoMLConfig(name='Automated ML Experiment',
                             task='classification',
                             primary_metric = 'AUC_weighted',
                             compute_target=aml_compute,
                             training_data = train_dataset,
                             validation_data = test_dataset,
                             label_column_name='Label',
                             featurization='auto',
                             iterations=12,
                             max_concurrent_iterations=4)

# Specify the primary metric

from azureml.train.automl.utilities import get_primary_metrics

get_primary_metrics('classification')

### 2. Submit an automated machine learning experiment

from azureml.core.experiment import Experiment

automl_experiment = Experiment(ws, 'automl_experiment')
automl_run = automl_experiment.submit(automl_config)

### 3. Retrieve the best run and its model

best_run, fitted_model = automl_run.get_output()
best_run_metrics = best_run.get_metrics()
for metric_name in best_run_metrics:
    metric = best_run_metrics[metric_name]
    print(metric_name, metric)
    
### 4. Explore preprocessing steps

for step_ in fitted_model.named_steps:
    print(step_)
    
