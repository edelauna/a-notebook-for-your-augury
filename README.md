# A Notebook for your Augury
au·gu·ry
> a sign of what will happen in the future; an omen.


# Todo:
* [x] Replace LabelEncoder with OrdinalEncoder for single columns
* [x] some sort of caching for unchanged models 
* [ ] add some better documentation into the notebook
* [ ] Refactor the whole `_guard` pattern applied throughout - there's probably a better way to do this.
    * added `overwrite=[True|False] for this
* [ ] Centralize Column naming logic (e.g. `"%s_clean" % c`, used too much)
* [ ] limited to <= 3 models atm - look into allowing n
* [ ] Best way to drop nulls when evaluating datasets in two parts (continuous vs. categorical)
* [ ] Best way to handle nulls (since also dropped from Test)
* [ ] Verify if I'm doing KMeans correctly
* [ ] Feature engineering to add new features (currently replaces existing)
* [ ] Load from Pickel
* [ ] Inject dependancies into functions for documentation purposes
* [ ] Loading data other than csv - e.g. sql
* [ ] Repetitive Way to perform Feature Engineering 
* [ ] Ability to model data from images (probably a differant notebook)
* [ ] Update Multilater Perception Models, add Naive Bayes boosting for things like NLP (probably a different notebook)