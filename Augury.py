class Augury:
  def constructor():
    """
    Decorator which adds funcs to this class    
    """
    def decorator(*funcs):
      for func in funcs:
        setattr(__class__, func.__name__, func)
    return decorator
  def _attr(self, *readers, overwrite=True, **writers):
    """
    Returns the relevent self.attr.
    Will also set a value if passed with a value.
      Parameters
      ----------
      readers : str
          attr to return
      overwrite : bool
          if False, will not set a value, if a value exists
      writers : Dict
          key as attr to return, value as value to set.
      Returns
      ----------
      tuple of ordered attrs
    """
    _attrs = []
    for attr in readers:
      _attrs.append(getattr(self,attr)) if hasattr(self, attr) else _attrs.append(None)
    for attr in writers:
      if not hasattr(self, attr) or overwrite:
        setattr(self, attr, writers[attr])
      _attrs.append(getattr(self,attr))
    return tuple(_attrs)
  def _hash(self, hash, *keys):
    """
    Helper function to destructure a hash.
    ...didn't end up using this as much
      Parameters
      ----------
      hash : Dictionary
          hash to destructure
      keys : str
          values at key will be returned.
      Returns
      ----------
      tuple of ordered hash values
    """
    results = []
    for key in keys:
      results.append(hash[key]) if key in hash else results.append(None)
    return tuple(results)

"""
TODO: move functions from Notebook to here, to add tests, and better
track changes. 
TODO: Load this class via pickle into jupyter notebook
"""
