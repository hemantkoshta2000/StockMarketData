from nsetools import Nse
nse = Nse()
# print(nse)
# print(nse.headers)
# print(nse.bhavcopy_base_filename)
# print(nse.nse_opener())
# print(nse.get_quote("reliance"))

q = nse.get_quote('infy', as_json=True)
from pprint import pprint
pprint(q)

