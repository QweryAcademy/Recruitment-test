class MyClass(object):
    def test_multiples_of_3_alone(self):
        self.assertTrue(fizzbuzz_val(3) is 'Fizz')
        self.assertTrue(fizzbuzz_val(99) is 'Fizz')
        self.assertFalse(fizzbuzz_val(15) is 'Fizz')
        self.assertFalse(fizzbuzz_val(8) is 'Fizz')
        self.assertEqual(fizzbuzz_val(15), 'FizzBuzz')
        self.assertTrue(fizzbuzz_val(5) is 'Buzz')
        self.assertTrue(fizzbuzz_val(10) is 'Buzz')
        self.assertTrue(fizzbuzz_val(20) is 'Buzz')
        self.assertFalse(fizzbuzz_val(8) is 'Buzz')
        
        def test_multiples_of_5_alone(self):
            pass

    def test_multiples_of_3_and_5(self):
        pass