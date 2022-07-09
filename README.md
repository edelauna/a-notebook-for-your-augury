# A Notebook for your Augury
au·gu·ry
> a sign of what will happen in the future; an omen.

Goal: Create a Notebook which can automate much of the machine learning minutiate duplicated across tasks.

Highlight: Got little bit over [80% on Titanic Spaceship Task]()

# Todo:
* [ ] add some better documentation into the notebook
* [ ] Add correlation heatmap visualization and process for dropping columns
* [ ] Add more visualization to test data processing for confirmation
* [ ] Improved encoding handling when column has bool types, mixed with a 3rd value for NaNs (currently using try, except)
* [ ] Centralize Column naming logic (e.g. `"%s_clean" % c`, used too much) 
    - maybe implement state machines per column?
* [ ] Load from Pickel
* [ ] Add tests - either Migrate code to Augury.py and add tests, or put them all in the last cell of notebook...
* [ ] Verify if I'm doing KMeans correctly
    * [ ] Automate how best num of clusters can be chosen
* [ ] Does the ##Fit section make sense?
* [ ] Implement ##Tune section (thinking to test against smaller feature set for performance check)
* [ ] Ability to model data from images (probably a differant notebook)
* [ ] Update Multilater Perception Models, add Naive Bayes boosting for things like NLP (probably a different notebook)
* [ ] Loading data other than csv - e.g. sql
* [ ] limited to <= 3 models atm - look into allowing n
    * [ ] Is (BayesSearchCV)[https://scikit-optimize.github.io/stable/modules/generated/skopt.BayesSearchCV.html] worth it?
        - runs a bit slower, but score is generally the same...
* [x] Replace LabelEncoder with OrdinalEncoder for single columns
* [x] some sort of caching for unchanged models 
* [X] Refactor the whole `_guard` pattern applied throughout - there's probably a better way to do this.
    * added `overwrite=[True|False]` for this
* [X] Inject dependancies into functions for documentation purposes
* [X] Repetitive Way to perform Feature Engineering 
    * [X] - on Test data
* [X] Best way to drop nulls when evaluating datasets in two parts (continuous vs. categorical)
* [X] Best way to handle nulls (since also dropped from Test)
* [X] Feature engineering to add new features (currently replaces existing)
    * [X] Encoding categorical engineered features, which were not present in training data. 