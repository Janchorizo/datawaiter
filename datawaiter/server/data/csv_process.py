import pandas as pd
from io import StringIO

class CSV:
	def __init__(self, csv_content):
		self._csv_content = csv_content
		self._csv_df = None
		self._processed_csv_df = None

		self.is_valid = self.__is_csv_valid()

		if self.is_valid:
			self._processed_df = self.__process_csv()

	def __is_csv_valid(self):
		is_valid = True

		is_valid = is_valid and len(self._csv_content) > 0

		csv_string_io = StringIO(self._csv_content)

		try:
			self._csv_df = pd.read_csv(csv_string_io)
		except Exception as e:
			is_valid = False
			print(e)
		
		is_valid = is_valid and not self._csv_df.empty

		return is_valid

	def __process_csv(self):
		try:
			self._processed_csv_df = self._csv_df.describe()
		except Exception as e:
			raise e

	def save_csv_df(self, location):
		self._csv_df.to_csv(location)

	def save_processed_csv_df(self, location):
		self._processed_csv_df.to_csv(location)