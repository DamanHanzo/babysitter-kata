import unittest
from babysitter import BabySitter
from notavailableexception import NotAvailableException

class BabySitterTests(unittest.TestCase):

	def setUp(self):	
		'''Setup the babysitter once so that it can't be utilized all throughout the test'''
		self.sitter = BabySitter(17, 21, 22)
		self.startTimeNotAvailableMsg = "I am not available before 5:00 PM, sorry"
		self.endTimeNotAvailableMsg = "I cannnot stay after 4:00 AM"
		
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
	
	def test_verify_entered_time_ranges(self):
		'''Validate the entered hours for the babysitter'''
		self.assertRaises(NotAvailableException, self.sitter._verifyTimeRanges, 17, 16, 21)
		self.assertRaises(NotAvailableException, self.sitter._verifyTimeRanges, 17, 5, 21)

	def test_adjust_hour(self):
		'''Test to make sure that the time is adjusted to match 24 hour time format'''
		self.assertEqual(self.sitter._adjustHour(2), 26)
		self.assertEqual(self.sitter._adjustHour(13), 13)

	def test_calc_hours_till_bed_time(self):
		'''Check if the hours till bedtime are calculate accurately'''
		hours = self.sitter._startTime - self.sitter._endTime
		self.assertEqual(self.sitter._calcHoursTillBedTime(), hours)

if __name__ == '__main__':
	unittest.main()