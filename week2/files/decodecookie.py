import pickle
import base64

cookie = "eyJyb2xlIjoiU3RhZmYiLCJ1c2VybmFtZSI6InVzZXIifQ.Y_hC4Q.gm17oSIlcdS5sNlFsNPcifnfqOc=="

parts = cookie.split(".")
cookie_data_b64 = parts[1]
cookie_data_bytes = base64.b64decode(cookie_data_b64)
cookie_data = pickle.loads(cookie_data_bytes)

print(cookie_data)

