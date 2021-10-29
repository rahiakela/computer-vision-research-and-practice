import jwt

priv_key = """MIIEowIBAAKCAQEAsFKVStR3a/vsXaQNRmN/zkF911Uy1KatxzIt30WmBW1Vq1NM
rAe/gnmA8riQMmDA9uzpNgnORxZKWT0sSVuLti1SC+WT19OtEjtrxXbAoNKFDQFm
vdFSU5iYpYXTX/SZRO2mW990DXsAMSJPEHuj6hLYKPUMYAKThn+5TsQ7SKrm5J9E
GZe04zB/ZMO3maz6CXGCj1Eh66fMxxpeJJkh+nWA47tgOYpgKMYzqMf6wFUqkHRi
mUGwpd8GqdTnLtRb7nbrmIqqAw7FmumGxgpn8GOJcnL+8ofWdtTyLyO41okQy0eJ
oIMNTsqLUhWlgdwzAfdwIX6nHRcIHVIveCYvHQIDAQABAoIBACQ5UyKEc+RjZTP3
uCJ13pPpMIlEn6TAeYMq8/GixXDn/WmtO1s8XEPZ4nv7HuS6q+oO0fqgGRjRo4Sh
5K9Nd2598RUwnScB/dR5ELMIqppfpaX+W7Uzg85Y00NuMvbLsZFPoZXOWnFKi8eM
XOHuBMbaCD6h2WEAJn7DTra36dYLru781jf3Bj9b0DIaRZQs/+kOkInDlLzm1Zos
n5Jlf63mQe2BO1WG7wwEINUuhk5u6zKAGej8PO7zTvZB6KVTijudz9nCoLz52PqW
WnV66zTGysxasq+EEtBJjuCPg/27wcewnn2GiqH+JeV0rF46W+4zUheOI4Shq9l9
yL24KaECgYEA3rmemn6ANPw6S/YJIq5PbQjtqEAqH6gBKjyzEAbrMDUr9XnBfiaL
4FxxxxE/fUkMODPtFPtFv8UubnpVqg3Hve0kA0N5vHCUEojb0NdzZ8qsX7GQdaiX
JNFfJ/b4ZCF6TU6XVQmx+wxhgq7/ysUQiX7EhQmVIBXxB/67MDvMfa8CgYEAyqo/
FJl4lFDKZuKW15Ki/K/tFQRjbLtLBHrYl+hYRHQZoiipP8wRbQhaQ6ZMzAMgTXKs
fHI2PQYap4TQVXsrp+iHeLEyfyX55tsAr3hzZNl4gIxNfMYVw6oXpm71jLxdG/L7
1p7vVovdP1PwjZAZgEe9By3PwzXmQew16KgtvvMCgYEAkXwcTvyc0H+FsQK4uu+z
sBxp6UJogZ8ji6x0pt5uGGJTIZjzvGx/aAHazFbG6xahJcE9dzwfNoIdr0q31EoG
FFjn8j3MMjwzbNv7AjMKDl1ENYnuO/zxJbqh9qALZpS7p+3TSlf3624N7+hR6+jH
wZiN0/0LbRcIB9nr+jjFfb8CgYB7srf32ciYNkujyo+pGm5y7uo1Fs2csyCRpm2H
IqClf3uZ11mef+7u7tcxTVK4fvv7aY/QEWH7kzs3nkAOvLQjszDkwLsCkmpatrdP
YqSEHJyJUZmGG91y5OG0iytC8EGgaom+MJoC6DFtks1Tim2WN7Mvq42RJ9fXytYI
oIXzcwKBgC4ZK1Fb3eH015/nNtr4i/xUnEgVHeUGdVAfAvzDiNO03wkterVvhcHA
OyiMJjxE0zSlBPgbYxr2m771Gg70R7NEkT+v0WQH+pSbFx+OuG07bElPkYzRbQ5N
tntj6/23Jk3a1BlRqaj0u3d21VJsDQbfsAuuhbWpbLzukFjuTSp+"""
private_key = "-----BEGIN RSA PRIVATE KEY-----\n"+priv_key+"\n-----END RSA PRIVATE KEY-----"

pub_key = """MIIDFTCCAf2gAwIBAgIUS5z0O0ZZxKlc9RL2cBqWKFdvbg4wDQYJKoZIhvcNAQEL
BQAwGjEYMBYGA1UEAwwPc3lub2RleC1laHItYXBpMB4XDTIxMTAyNzA5NTkyMFoX
DTIxMTEyNjA5NTkyMFowGjEYMBYGA1UEAwwPc3lub2RleC1laHItYXBpMIIBIjAN
BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsFKVStR3a/vsXaQNRmN/zkF911Uy
1KatxzIt30WmBW1Vq1NMrAe/gnmA8riQMmDA9uzpNgnORxZKWT0sSVuLti1SC+WT
19OtEjtrxXbAoNKFDQFmvdFSU5iYpYXTX/SZRO2mW990DXsAMSJPEHuj6hLYKPUM
YAKThn+5TsQ7SKrm5J9EGZe04zB/ZMO3maz6CXGCj1Eh66fMxxpeJJkh+nWA47tg
OYpgKMYzqMf6wFUqkHRimUGwpd8GqdTnLtRb7nbrmIqqAw7FmumGxgpn8GOJcnL+
8ofWdtTyLyO41okQy0eJoIMNTsqLUhWlgdwzAfdwIX6nHRcIHVIveCYvHQIDAQAB
o1MwUTAdBgNVHQ4EFgQUKwfHYsWhr/juPzr2E0Fm7n55vGcwHwYDVR0jBBgwFoAU
KwfHYsWhr/juPzr2E0Fm7n55vGcwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0B
AQsFAAOCAQEAlRwbKgVLgGlOo1n3R676ISulTOtqxSsVvLmbMGHyjOOVsjzna95Q
OZD6k+YxgHltS8Rz4QbWEBLMx3MvblSNFZhgCEGu8SuxigHpAWjBsqhFKtHW0PAk
DCS1r+tYRRSe8jD5WIbseCWeMwqJONYZ9zOX4Z7LrmlxTDlyukV2vWqLxSTIPIr+
abpt7qGOQET3egLSjN10PLLKY/0FU59igKJN/uxnHR51UyNM5Hc528VHqUxjdgbN
7NFKnj5HP4SQxcSO4KWYNQFrb3OPwbDrKlTcP8wi2kAJvR/r/zzBIY30umZbwt7W
CUkSEZStKQejPrC2Yzl2XwaAzpwvbBiphg==
"""
public_key = "-----BEGIN CERTIFICATE-----\n" + pub_key + "\n-----END CERTIFICATE-----"

headers = {
    "alg": "RS256",
    "typ": "JWT"
}
payload = {
  "iss": "cc354572-37bd-4a86-9a24-3d210e70db0d",
  "sub": "cc354572-37bd-4a86-9a24-3d210e70db0d",
  "aud": "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token",
  "jti": "f9eaafba-2e49-11ea-1180-5ce0c5aee679",
  "exp": 1583524402
}

encoded = jwt.encode(payload, private_key, algorithm="RS256")
print(encoded)

decoded = jwt.decode(encoded, public_key, options={"verify_signature": False})
print(decoded)
