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