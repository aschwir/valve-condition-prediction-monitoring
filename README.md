## Dataset & Attribution

This project uses the **Condition Monitoring of Hydraulic Systems** dataset from the UCI Machine Learning Repository, originally collected by the ZeMA (Center for Mechatronics and Automation Technology) in Saarbrücken, Germany.

* **Source:** [UCI Machine Learning Repository – Condition Monitoring of Hydraulic Systems](https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems)
* **Creators:** Nikolai Helwig, Eliseo Pignanelli, and Andreas Schütze (2018)
* **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Notes for preprocessing data**
* *CSV file used for model training is located in `process_train_data/processed_data.csv`*
* *Training data consists of the mean, median, and standard deviation of each valve per cycle.*

### Target Valve Condition Labels (`profile.txt`)
* **`100`:** Optimal switching behavior
* **`90`:** Small lag
* **`80`:** Severe lag
* **`73`:** Close to total failure

### Sensors
* **Pressure sensors** `(PS1-6)`
* **Motor power sensor** `(EPS1)`
* **Volume flow sensors** `(FS1/2)`
* **Temperature sensors** `(TS1-4)`
* **Vibration sensor** `(VS1)`
* **Efficiency factor** `(SE)`
* **Virtual cooling efficiency sensor** `(CE)`
* **Virtual cooling power sensor** `(CP)`


## Model Performance

The Random Forest baseline achieved **0.986 accuracy** and **0.983 macro F1** 
on the held-out test set. Stratified 10-fold cross-validation on the training data gave a 
mean accuracy of **0.980** and macro F1 of **0.974**, which is consistent with the 
baseline and indicates the result is stable across different data splits.

| Metric      | Baseline (Test Set) | Cross-Validation (10-Fold) |
|-------------|---------------------|----------------------------|
| Accuracy    | 0.986               | 0.980                      |
| Macro F1    | 0.983               | 0.974                      |
| Weighted F1 | 0.987               | 0.980                      |