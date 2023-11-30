import numpy as np 
import matplotlib.pyplot as pl

# Muuttujat : 
dt = 1                # aika-askel [s]
v = 12155.55             # pakonopeus Maasta [m/s]
G = 6.67384*10**(-11)    # gravitaatiovakio [N*m^2*kg*s^(-2)]
m_maa = 5.9737*10**24    # Maan massa [kg]
m_kuu = 7.342*10**22     # Kuun massa [kg]
L = 384400000            # Maan ja Kuun keskipisteiden etäisyys [m]
y_kuu = 178710           # raketin loppuetäisyys Kuun keskipisteestä, johon raketin tulee päästä, Kuun säde + 50km [m]
y = 6411000              # raketin alkukorkeus Maan keskipisteestä, lähtökorkeus + Maan säde [m]
                         # ilmanvastusta ei huomioida, sillä lähtökorkeus on ilmakehän yläpuolella 
t = 0.0                  # alkuhetki [s]
tt = np.array([t])       # ensimmäiset datapisteet
yt = np.array([y])

while y < L-y_kuu : 
    t = t+dt             # päivitetään aika 
    a = -(G*m_maa/y**2)+(G*m_kuu/(L-y)**2) # päivitetään kiihtyvyys

    v = v+a*dt           # päivitetään nopeus
    v_avg = (2*v-a*dt)/2 # keskinopeus
    y = y+v_avg*dt       # päivitetään paikka
    print(a)             # tulostetaan kiihtyvyyden dataa, tähän voisi vaihtaa myös esim. aika (t)
    tt = np.append(tt,t)
    yt = np.append(yt,y)

pl.plot(tt,yt, 'k')
pl.xlabel('t (s)')
pl.ylabel('y (m)')
pl.show()
print('Matkaan kulunut aika on ' + str(t) + ' s')
print('Kuljettu matka on ' + str(y) + ' m')