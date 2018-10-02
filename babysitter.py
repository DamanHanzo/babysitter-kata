class BabySitter:

	def __init__(self, startTime, endTime, bedTime):
		self._startTime = startTime
		self._endTime = endTime
		self._bedTime = bedTime
		self._sitterStartTime = 17
		self._sitterEndTime = 4
		self._initialBedTime = 21

	def sitter_start_time(self):
		return self._sitterStartTime

	def sitter_end_time(self):
		return self._sitterEndTime

	def initial_bed_time(self):
		return self._initialBedTime