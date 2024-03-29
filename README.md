# A Notebook for your Augury
au·gu·ry
> a sign of what will happen in the future; an omen.

Goal: Create a Notebook which can act as a boilerplate, and help automate much of the machine learning minutiate duplicated across tasks.

Open [A_Notebook_for_your_Augury.ipynb](A_Notebook_for_your_Augury.ipynb) in Google Colab for quick review.

Highlight: Got little bit over [80% on Titanic Spaceship Task](https://www.kaggle.com/code/elliottdelaunay/spaceship-titanic-augury-template?scriptVersionId=100361258)

# Todo:
Pad where I'm listing items I'd like to do, as I learn about machine _learning_ and python. 
* [ ] Refactor plotting logic so that it's generic
* [ ] Add section for ensuring all dependancies are installed
* [ ] Figure out some better pattern to apply... a notebook with differant methods all over the places is making it confusing to iterate on
* [ ] Refactor processing and add rules flow - lots of duplicate input_guards
* [ ] Centralize Column naming logic (e.g. `"%s_clean" % c`, used too much) 
    - maybe implement state machines per column?
* [ ] Add more visualization to test data processing for confirmation
* [ ] Improved encoding handling when column has bool types, mixed with a 3rd value for NaNs (currently using try, except)
* [ ] Move everything in Python Main Class and then Load from Pickel?
* [ ] Add tests - either Migrate code to Augury.py and add tests, or put them all in the last cell of notebook...
* [ ] Add some variability to Kaggle and google drive integrations
* [X] Verify if I'm doing KMeans correctly
    * [ ] Automate how best num of clusters can be chosen
* [ ] Does the ##Fit section make sense?
* [ ] Implement ##Tune section (thinking to test against smaller feature set [e.g.`augur.X_compress_train`] for performance check)
* [ ] Ability to model data from images (probably a differant notebook)
* [ ] Update Multilayer Perception Models, add Naive Bayes boosting for things like NLP (probably a different notebook)
* [ ] Loading data other than csv - e.g. sql
* [ ] limited to <= 3 models atm - look into allowing n
    * [ ] Is (BayesSearchCV)[https://scikit-optimize.github.io/stable/modules/generated/skopt.BayesSearchCV.html] worth it?
        - runs a bit slower, but score is generally the same...
* [X] Add null type plots vs text report
* [X] Refactor input guard to throw exception (asserts are removed)
* [X] Visualize outlier detection - add lower for clip
* [X] Add correlation heatmap visualization and process for dropping columns
* [X] Add missing map enhancement `missingno`
* [x] Replace LabelEncoder with OrdinalEncoder for single columns
* [x] some sort of caching for unchanged longer running functions 
* [X] Refactor the whole `_guard` pattern applied throughout - there's probably a better way to do this.
    * added `overwrite=[True|False]` for this
* [X] Inject dependancies into functions for documentation purposes
* [X] Repetitive Way to perform Feature Engineering 
    * [X] - on Test data
* [X] Best way to drop nulls when evaluating datasets in two parts (continuous vs. categorical)
* [X] Best way to handle nulls (since also dropped from Test)
* [X] Feature engineering to add new features (currently replaces existing)
    * [X] Encoding categorical engineered features, which were not present in training data. 

# Development
Using docker and VS Code with Python and Jupyter extensions so that it's easier to track changes.
2. ` docker run -p 9545:8888 -e JUPYTER_TOKEN="bigEnotation" -v $pwd:/home/jovyan/work jupyter/scipy-notebook`
  3. Should output a server url and token, in VS Code there should be an option at the bottom of the screen to connect to a Jupyter Server - click that and then paste the link.
  4. Will Need to change Kernel (top right of VsCode when notebook is open)
  5. Might need to pip intall some dependancies (e.g. google-colab)