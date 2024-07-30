import secrets
import string as s

random = secrets.SystemRandom()

aleatorio = s.ascii_letters + s.digits + s.punctuation

senha = random.choices(aleatorio, k=10)

senha = "".join(senha)

print(senha)
