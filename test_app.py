import unittest,pandas as pd
from app import summarize
class Test(unittest.TestCase):
 def test_sum(self):
  r=summarize(pd.DataFrame({'g':['a','a','b'],'v':[1,2,4]}),'g','v');self.assertEqual(r.loc[0,'sum'],3)
