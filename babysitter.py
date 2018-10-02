from notavailableexception import NotAvailableException

class BabySitter:

	def __init__(self, startTime, endTime, bedTime):
		self._sitterStartTime = 17
		self._sitterEndTime = 4
		self._initialBedTime = 21
		self._hourlyWageTillBedTime = 12
		self._hourlyWageBedTimeTillMidnight = 8
		self._hourlyWageMidnightTillEnd = 16
		self._verifyTimeRanges(startTime, endTime, bedTime)

	def _verifyTimeRanges(self, startTime, endTime, bedTime):
		'''Check to make sure that the input time meets the sitter's time constraints'''
		if startTime < self._sitterStartTime and startTime > self._sitterEndTime:
			raise NotAvailableException("I am not available before 5:00 PM, sorry")
		elif endTime < self._sitterStartTime and endTime > self._sitterEndTime:
			raise NotAvailableException("I cannnot stay after 4:00 AM")
		else:
			self._startTime = self._adjustHour(startTime)
			self._endTime = self._adjustHour(endTime)
			self._bedTime = self._adjustHour(bedTime)

	def _adjustHour(self, hour):
		'''Adjust time to match 24 hour time format'''
		if hour >= 0 and hour <= 4:
			hour += 24
		return hour

	def _calcHoursTillBedTime(self):
		'''Method to calculate hours from start time till bed time'''
		if self._endTime < self._bedTime:
			return self._endTime - self._startTime
		return self._bedTime - self._startTime

	def _calcHoursBedTimeTillMidnight(self):
		'''Method to calculate hours from bed time till midnight'''
		if self._endTime < self._bedTime:
			return 0
		if self._endTime < 24:
			return self._endTime - self._bedTime
		return 24 - self._bedTime

	def _calcHoursMidnightTillEnd(self):
		'''Method to calculate hours from midnight till the end'''
		if self._endTime <= 24:
			return 0
		return self._endTime - 24

	def total_wages_earned(self):
		'''Evaluates and returns total earned wages'''
		return int(((self._hourlyWageTillBedTime * self._calcHoursTillBedTime()) + 
			(self._hourlyWageBedTimeTillMidnight * self._calcHoursBedTimeTillMidnight()) +
			 (self._hourlyWageMidnightTillEnd * self._calcHoursMidnightTillEnd())))

	def sitter_start_time(self):
		return self._sitterStartTime

	def sitter_end_time(self):
		return self._sitterEndTime

	def initial_bed_time(self):
		return self._initialBedTime

	def hourly_wage_till_bed_time(self):
		return self._hourlyWageTillBedTime

	def hourly_wage_bedtime_till_midnight(self):
		return self._hourlyWageBedTimeTillMidnight

	def hourly_wage_midnight_till_end(self):
		return self._hourlyWageMidnightTillEnd

	def set_sitter_start_time(self, startTime=None):
		if startTime is not None:
			self._sitterStartTime = int(startTime)

	def set_sitter_end_time(self, endTime=None):
		if endTime is not None:
			self._sitterEndTime = int(endTime)

	def set_initial_bed_time(self, bedTime=None):
		if bedTime is not None:
			self._initialBedTime = int(bedTime)

	def set_hourly_wage_till_bed_time(self, wageRate=None):
		if wageRate is not None:
			self._hourlyWageTillBedTime = wageRate

	def set_hourly_wage_bedtime_till_midnight(self, wageRate=None):
		if wageRate is not None:
			self._hourlyWageBedTimeTillMidnight = wageRate

	def set_hourly_wage_midnight_till_end(self, wageRate=None):
		if wageRate is not None:
			self._hourlyWageMidnightTillEnd = wageRate