import math
ang = float(input("digite o ângulo que você deseja"))
seno = math.sin(math.radians(ang)) 
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians (ang))
print("0 ângulo de () tem seno de {:.2f}".format(ang, seno))
print("O angulo de () tem coseno de {:.2f}".format(ang, cose))
print("0 ângulo de () tem tångente de {:.2f}".format(ang,tang))
