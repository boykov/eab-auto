import string
from urllib2 import urlopen         
 
u = urlopen("http://python.org")    
words = {}                          
                                    
for line in u.readlines():          
    line = string.strip(line, " \n")    
    for word in line.split(" "): 
        try:                            
            words[word] += 1            
        except KeyError:                
            words[word] = 1             
 
pairs = words.items()               
                                    
pairs.sort(lambda a, b: b[1]-a[1])  
 
for p in pairs[:10]:                
    print p[0], p[1]


a = [i for i in range(0,3,1)]
print a[3:0:-1]
print a

print string.digits

import unittest

class IntegerArithmenticTestCase(unittest.TestCase):
    """Example of using unittest
    """
    def testAdd(self):
        """Test method names begin 'test+'

        Arguments:
        - `self`:
        """
        self.assertEquals((1 + 2), 3)
        self.assertEquals((0 + 1), 1)

    def testMultiply(self):
        self.assertEquals((0 * 10), 0)
        self.assertEquals((5 * 8), 40)

# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(IntegerArithmenticTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)







