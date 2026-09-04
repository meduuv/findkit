import tempfile,unittest
from pathlib import Path
from findkit import find,find_suffix
class Tests(unittest.TestCase):
 def test_find(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);(p/"a.py").write_text("");(p/"b.txt").write_text("")
   self.assertEqual(len(find(p)),2);self.assertEqual(find_suffix(p,"py")[0].endswith("a.py"),True)
if __name__=="__main__":unittest.main()
