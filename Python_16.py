from math import cos, tan, radians, sin
ang = float(input('Digite o valor do angulo: '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print(f'O angulo {ang} \nSeno {sen:.2f} \nCosseno {coss:.2f} ')
print(f'Tangente {tang:.2f}')
