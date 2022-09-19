from this import d
import unittest
def reversa (thislist):
    return thislist[::-1]


def isPalindrome(thislist):
    listareversa=reversa(thislist)
    return listareversa==thislist
    
def coins(valor):
    dinero={'500':0,'100':0,'50':0,'10':0,'5':0,'1':0}
    dinero['500']=int(valor/500)
    valor=valor%500
    dinero['100']=int(valor/100)
    valor=valor%100
    dinero['50']=int(valor/50)
    valor=valor%50
    dinero['10']=int(valor/10)
    valor=valor%10
    dinero['5']=int(valor/5)
    valor=valor%5
    dinero['1']=valor
    return dinero 


def factorial_recursiva(valor):
    if valor==1:
        return 1
    else:
        return valor*factorial_recursiva(valor-1)
    
def fibonacci_recursiva(n):
    fib = [0, 1]
    while len(fib)< n:
        y = fib[len(fib) - 1] + fib[len(fib) - 2]
        fib.append(y)
    return fib

class Test(unittest.TestCase):
    def testReverse(self):
        self.assertEqual (reversa([1,3,5]), [5,3,1])
        self.assertEqual (reversa([7,8,9]),[9,8,7])
    def test_palindrome(self):
        self.assertTrue(isPalindrome('racecar'))
        self.assertFalse(isPalindrome('roca'))
        self.assertTrue(isPalindrome('ana'))
        self.assertTrue(isPalindrome('allulla'))
        self.assertTrue(isPalindrome('sometemos'))
    def test_coins(self):
        self.assertEqual(coins(870), {'500':1,'100':3,'50':1,'10':2,'5':0,'1':0} )
        self.assertEqual(coins(850), {'500':1,'100':3,'50':1,'10':0,'5':0,'1':0} )
        self.assertEqual(coins(840), {'500':1,'100':3,'50':0,'10':4,'5':0,'1':0} )
        self.assertEqual(coins(830), {'500':1,'100':3,'50':0,'10':3,'5':0,'1':0} )
        self.assertEqual(coins(820), {'500':1,'100':3,'50':0,'10':2,'5':0,'1':0} )
    def test_recursivo(self):
        self.assertEqual(factorial_recursiva(5),120)
        self.assertEqual(factorial_recursiva(3),6)
        self.assertEqual(factorial_recursiva(4),24)
    def test_fibonacci(self):
        self.assertEqual(fibonacci_recursiva(6),[0,1,1,2,3,5])



if __name__=='__main__':
    unittest.main()
