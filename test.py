from opensky_api import OpenSkyApi
import os
import keyboard
import time
api = OpenSkyApi("ClockworkKettle", "tcPzTiY@tE3jW2R")
iterations_of_main_loop=0
my_lat = 53.37614
my_long = -6.59135
distance =3.2
#pass = tcPzTiY@tE3jW2R
while (True):

    i=0
    states = api.get_states()
    os.system('cls')
    print("===============================================")
    print("Hold q to exit")
    print("My Co-ordinates: %f %f" %(my_lat, my_long))
    print("Bounding Box: \nUpper Bounds: %f %f" %(my_lat+distance, my_long+distance))
    print("Lower Bounds: %f %f" %(my_lat-distance, my_long-distance))
    for s in states.states:
        if (s.longitude is not None) or (s.latitude is not None):
            aircraft_longitude = float("%r" % s.longitude)
            aircraft_latitude = float("%r" % s.latitude)
            if (my_lat+distance > aircraft_latitude and my_lat - distance < aircraft_latitude) and (my_long + distance > aircraft_longitude and my_long - distance < aircraft_longitude):
                #print("(%r, %r, %r, %r, Country of Origin: %r, Callsign: %r, Icao24: %r)" %
                #(s.longitude, s.latitude, s.baro_altitude, s.velocity, s.origin_country, s.callsign, s.icao24))
                print("%r, \tLatitude: %r, \tLongitude: %r, \tVelocity: %r, \tHeading: %r" % (s.callsign, s.latitude, s.longitude, s.velocity, s.heading))
                i+=1
    iterations_of_main_loop +=1
    print("Number of entries: %i" % i)
    print("Iteration: %i" %iterations_of_main_loop)
    print("===============================================")


    if (keyboard.is_pressed('q')):
        break
    time.sleep(6)
