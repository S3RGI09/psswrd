#!/usr/bin/python3

from random import choice
print("\033[1;31m"+" ____  ____ ______        ______  ____  ")
print("\033[1;31m"+"|  _ \/ ___/ ___\ \      / /  _ \|  _ \ ")
print("\033[1;31m"+"| |_) \___ \___ \\ \ /\ / /| |_) | | | |")
print("\033[1;31m"+"|  __/ ___) |__) |\ V  V / |  _ <| |_| |")
print("\033[1;31m"+"|_|   |____/____/  \_/\_/  |_| \_\____/ ")
print("---------------------------------------------------------------")

print("\033[1;33m"+"[Info] Script para crear una contraseña muy segura aleatoriamente"+'\033[0;m') 
print("\033[1;36m"+"  ||   Programada por S3RGI09 (Sergio Casero Verdial) ")
print("\033[1;35m"+"* IG: s3rgi09__ | GitHub: S3RGI09"+'\033[0;m')
print("\033[1;34m"+"---------------------------------------------------------------")
longitud = 18
valores = "0123456789abcdefghijklmnopqrstuvwxyzñüöäïëçABCDEFGHIJKLMNOPQRSTUVWXYZÑÜÖÄÏËÇ"

p = ""
p = p.join([choice(valores) for i in range(longitud)])
print("\033[1;34m"+"La contraseña es: ")
print(p)
