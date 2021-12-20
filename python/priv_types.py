

class Dict(obejct):
	def __init__(self, inpt: any):
		pass

	def _convDict(self) -> object:
		return dict(self.inpt)

	def _convStr(self, delim: chr = ';') -> object:
		return "from _convStr"

	def _convNum(self) -> object:
		return "from _convNum"

	def __getitem__(self, key: any) -> any:
		pass

	def __setitem__(self, key: any) -> any:
		pass

	def __delitem__(self, key: any) -> any:
		pass

	def __iter__(self) -> any:
		pass

	def __str__(self) -> str:
		pass

a: dict[int, int] = {1:1}
b: str = "Hello world"
c: int = 11

print(Dict(a), Dict(b), Dict(c))
