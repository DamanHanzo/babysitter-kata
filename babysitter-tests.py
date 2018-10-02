import unittest

class BabySitterTests(unittest.TestCase):

	def setUp(self):	
		'''Setup the babysitter once so that it can't be utilized all throughout the test'''
		self.sitter = BabySitter(17, 21, 22)
		
	def test_if_babysitter_object_exists(self):
		'''Test if the babysitter object exists'''
		self.assertIsNotNone(self.sitter)
	
if __name__ == '__main__':
	unittest.main()