import unittest
from babysitter import BabySitter

class BabySitterTests(unittest.TestCase):

	def setUp(self):	
		'''Setup the babysitter once so that it can't be utilized all throughout the test'''
		self.sitter = BabySitter(17, 21, 22)
		
	def test_if_babysitter_object_exists(self):
		'''Test if the babysitter object exists'''
		self.assertIsNotNone(self.sitter)

	def test_initial_time_constraint(self):
		'''Check to make sure that the supplied time constants are set correctly'''
		self.assertEqual(self.sitter.sitter_start_time(), 17)
		self.assertEqual(self.sitter.sitter_end_time(), 4)
		self.assertEqual(self.sitter.initial_bed_time(), 21)

	def test_setting_sitter_time_constraints(self):
		'''Verify if the initial sitter time contraints can be updated from the initial values'''
		self.sitter.set_sitter_start_time(18)
		self.sitter.set_sitter_end_time(24)
		self.sitter.set_initial_bed_time(22)
		self.assertEqual(self.sitter.sitter_start_time(), 18)
		self.assertEqual(self.sitter.sitter_end_time(), 24)
		self.assertEqual(self.sitter.initial_bed_time(), 22)
	
if __name__ == '__main__':
	unittest.main()