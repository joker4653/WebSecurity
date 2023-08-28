import pickle
import base64

cookie = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Nzg3NzkxMTEsImJhbGFuY2UiOjJ9.WFDcNBSsaiWmVgwu5_nV6lTWiHuHcKAIulrTFhSmmmE"

parts = cookie.split(".")
cookie_data_b64 = parts[1]
cookie_data_bytes = base64.b64decode(cookie_data_b64)
cookie_data = pickle.loads(cookie_data_bytes)

print(cookie_data)

