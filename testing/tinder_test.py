import unittest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + '/../src')

import tinder

class tinderTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(tinder.tinder(["swimming", "gaming", "python", "anime"], ["tennis", "java", "anime"]), "like")
    
    def test2(self):
        self.assertEqual(tinder.tinder(["emacs", "photography", "skydiving"], ["poetry", "guitar", "singing", "painting", "vim"]), "dislike")
    
    def test3(self):
        self.assertEqual(tinder.tinder(["forestry", "cosplay", "kpop", "squirrel hunting", "sleeping"], ["forestry", "kpop", "cosplay", "television"]), "super like")
        
if __name__ == '__main__':
    unittest.main()