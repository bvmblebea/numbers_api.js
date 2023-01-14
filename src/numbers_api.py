from requests import get
	
class NumbersAPI:
	def __init__(self) -> None:
		self.api = "http://numbersapi.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}

	def get_number_fact(
			self,
			number: int | str,
			type: str = "trivia",
			not_found: str = None) -> dict:
		"""
		Get fact about the number
		Parameters:
			number: (int | str): integer, string <number> if type is date: -> <month/day>
			type: (str): string <trivia, math, date, year> -> default: <trivia>
			not_found: (str): string <default, floor, ceil>
		Returns: 
			dict: fact about the number
		"""
		url = f"{self.api}/{number}/{type}"
		if not_found:
			url += f"?notfound={not_found}"
		return get(
			f"{url}?json",
			headers=self.headers).json()


	def get_random_fact(
			self,
			type: str,
			min: int = None,
			max: int = None) -> dict:
		"""
		Get random fact
		Parameters:
			type: (str): string <math, date, year>
			min: (int): integer <minimum range of values>
			max: (int): integer <maximum range of values>
		Returns: 
			dict: random fact
		"""
		return get(
			f"{self.api}/random/{type}?json",
			headers=self.headers).json() 
