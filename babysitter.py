from notavailableexception import NotAvailableException

class BabySitter:

	def __init__(self, startTime, endTime, bedTime):
		self._startTime = startTime
		self._endTime = endTime
		self._bedTime = bedTime
		self._sitterStartTime = 17
		self._sitterEndTime = 4
		self._initialBedTime = 21

	def _verifyTimeRanges(self, startTime, endTime, bedTime):
		'''Check to make sure that the input time meets the sitter's time constraints'''
		if startTime < self._sitterStartTime and startTime > self._sitterEndTime:
			raise NotAvailableException("I am not available before 5:00 PM, sorry")
		elif endTime < self._sitterStartTime and endTime > self._sitterEndTime:
			raise NotAvailableException("I cannnot stay after 4:00 AM")

	def sitter_start_time(self):
		return self._sitterStartTime

	def sitter_end_time(self):
		return self._sitterEndTime

	def initial_bed_time(self):
		return self._initialBedTime

	def set_sitter_start_time(self, startTime=None):
		if startTime is not None:
			self._sitterStartTime = int(startTime)

	def set_sitter_end_time(self, endTime=None):
		if endTime is not None:
			self._sitterEndTime = int(endTime)

	def set_initial_bed_time(self, bedTime=None):
		if bedTime is not None:
			self._initialBedTime = int(bedTime)