Analyze model fairness with Fairlearn-
Fairlearn is a Python package that you can use to analyze models and evaluate disparity between predictions and prediction performance for one or more sensitive features.

It works by calculating group metrics for the sensitive features you specify. The metrics themselves are based on standard scikit-learn model evaluation metrics, such as accuracy, precision, or recall for classification models.

The Fairlearn API is extensive, offering multiple ways to explore disparity in metrics across sensitive feature groupings. For a binary classification model, you might start by comparing the selection rate (the number of positive predictions for each group) by using the selection_rate function. This function returns the overall selection rate for the test dataset. You can also use standard sklearn.metrics functions (such as accuracy_score, precision_score, or recall_score) to get an overall view of how the model performs.

Then, you can define one or more sensitive features in your dataset with which you want to group subsets of the population and compare selection rate and predictive performance. Fairlearn includes a MetricFrame function that enables you to create a dataframe of multiple metrics by the group.

Integration with Azure Machine Learning-
Fairlearn integrates with Azure Machine Learning by enabling you to run an experiment in which the dashboard metrics are uploaded to your Azure Machine Learning workspace. This enables you to share the dashboard in Azure Machine Learning studio so that your data science team can track and compare disparity metrics for models registered in the workspace.

Mitigation algorithms and parity constraints
The mitigation support in Fairlearn is based on the use of algorithms to create alternative models that apply parity constraints to produce comparable metrics across sensitive feature groups. Fairlearn supports the following mitigation techniques.

MITIGATION ALGORITHMS AND PARITY CONSTRAINTS
Technique	Description	Model type support
Exponentiated Gradient	A reduction technique that applies a cost-minimization approach to learning the optimal trade-off of overall predictive performance and fairness disparity	Binary classification and regression
Grid Search	A simplified version of the Exponentiated Gradient algorithm that works efficiently with small numbers of constraints	Binary classification and regression
Threshold Optimizer	A post-processing technique that applies a constraint to an existing classifier, transforming the prediction as appropriate	Binary classification
The choice of parity constraint depends on the technique being used and the specific fairness criteria you want to apply. Constraints in Fairlearn include:

Demographic parity: Use this constraint with any of the mitigation algorithms to minimize disparity in the selection rate across sensitive feature groups. For example, in a binary classification scenario, this constraint tries to ensure that an equal number of positive predictions are made in each group.
True positive rate parity: Use this constraint with any of the mitigation algorithms to minimize disparity in true positive rate across sensitive feature groups. For example, in a binary classification scenario, this constraint tries to ensure that each group contains a comparable ratio of true positive predictions.
False-positive rate parity: Use this constraint with any of the mitigation algorithms to minimize disparity in false_positive_rate across sensitive feature groups. For example, in a binary classification scenario, this constraint tries to ensure that each group contains a comparable ratio of false-positive predictions.
Equalized odds: Use this constraint with any of the mitigation algorithms to minimize disparity in combined true positive rate and false_positive_rate across sensitive feature groups. For example, in a binary classification scenario, this constraint tries to ensure that each group contains a comparable ratio of true positive and false-positive predictions.
Error rate parity: Use this constraint with any of the reduction-based mitigation algorithms (Exponentiated Gradient and Grid Search) to ensure that the error for each sensitive feature group does not deviate from the overall error rate by more than a specified amount.
Bounded group loss: Use this constraint with any of the reduction-based mitigation algorithms to restrict the loss for each sensitive feature group in a regression model.


