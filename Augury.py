class Augury:
  def constructor_(cls, **deps):
    """
    Sets helper functions on the empty initialized class
    
      Parameters
      ----------
      cls: object
        The pythong Class to add helper methods toos
      **deps: Dictionary
        Dictionary of dependancies which helper methods will need
    """
    def decorator(func):
      def _wrapper(self, *args, **kwargs): 
        func(self, *args, **{**deps, **kwargs})
      setattr(cls, func.__name__, _wrapper)
      _wrapper.__name__ = func.__name__
      _wrapper.__doc__ = func.__doc__
    return decorator

  """
  Example helper method
    def foo(self, **kwargs):
    \""" Need to explicilty check for dependancies \"""
  np = kwargs.get("np")
  print(np.random.rand(3,2))
  """

"""
Proof of concept from notebook for loading pickle

import joblib
joblib.dump(Augury,"./Augury.pkl")

_Augury = joblib.load("./Augury.pkl")

import numpy as np
# Note Augury must be a class within the notebook
# np is an example of dependancy injection
# Could probably do this in some kind of loop. 
_Augury.constructor_(Augury, np=np)(_Augury.foo)
"""