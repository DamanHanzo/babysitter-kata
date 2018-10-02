class NotAvailableException(Exception):
	def __init__(self, notAvailableMsg):
		Exception.__init__(self, notAvailableMsg)
		self.notAvailableMsg = notAvailableMsg