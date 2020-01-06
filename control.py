#! /usr/bin/python

# Imports
import RPi.GPIO as GPIO
import time
import requests

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)

# Turn off GPIO warnings
#GPIO.setwarnings(False)

# Set a variable to hold the GPIO Pin identity
passenger_front = 18
passenger_rear = 17
driver_front = 16
driver_rear = 27
switch = 21

# Set GPIO pin as input
GPIO.setup(passenger_front, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(passenger_rear, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(driver_front, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(driver_rear, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables to hold the current and last states
p_f = False
p_r = False
d_f = False
d_r = False
s = False
l_bright = 0.0;
r_bright = 0.0;

try:
        print("Waiting for PIR to settle ...")

        print("    Ready")
           # Loop until users quits with CTRL-C
        while True:
            # Read PIR state
            p_f = GPIO.input(passenger_front)
            p_r = GPIO.input(passenger_rear)
            d_f = GPIO.input(driver_front)
            d_r = GPIO.input(driver_rear)
            s = GPIO.input(switch)
            ''' 
            print("States: ")
            print("Driver front: ", d_f)
            print("Driver rear: ", d_r)
            print("Passenger front: ", p_f)
            print("Passenger rear: ", p_r)
            print("Switch: ", s)
            time.sleep(1)
            '''
            if (p_f == 0):
              if (r_bright > 0.00):
                r_bright = 0.00
              else:
                r_bright = 1.00   #Todo: Create variable to hold old brightness so it goes to old brightness when turned on.
              requests.post('https://maker.ifttt.com/trigger/brightness_change/with/key/dCzU4NlLSnMRRWnvw0rBjox7kEM0SveLTf0ed4zHXAn', params={"value1":r_bright,"value2":"none","value3":"none"})
              print("Desk lamp changed")
              time.sleep(0.2)
 



            old_r_bright = r_bright
            old_l_bright = l_bright
            if (s == 1):
              if (p_r == 1):
                r_bright = r_bright + 0.25
                print("Up")
              if (d_r == 1):
                r_bright = r_bright - 0.25
                print("Down")
              if (r_bright > 1.00):
                r_bright = 1.00
              elif (r_bright < 0.00):
                r_bright = 0.00
              if (r_bright != old_r_bright):
                requests.post('https://maker.ifttt.com/trigger/brightness_change/with/key/dCzU4NlLSnMRRWnvw0rBjox7kEM0SveLTf0ed4zHXAn', params={"value1":r_bright,"value2":"none","value3":"none"})
                print("brightness changed")
            else:
              if (p_r == 1):
                l_bright = l_bright + 0.25
              if (d_r == 1):
                l_bright = l_bright - 0.25
              if (l_bright > 1.00):
                l_bright = 1.00
              elif (l_bright < 0.00):
                l_bright = 0.00
            time.sleep(0.2)
                #r = requests.post('https://maker.ifttt.com/trigger/brightness_change/with/key/dCzU4NlLSnMRRWnvw0rBjox7kEM0SveLTf0ed4zHXAn', params={"value1":brightness,"value2":"none","value3":"none"})
                #r = requests.post('https://maker.ifttt.com/trigger/brightness_change/with/key/dCzU4NlLSnMRRWnvw0rBjox7kEM0SveLTf0ed4zHXAn', params={"value1":brightness,"value2":"none","value3":"none"})
            

            """# If the PIR is triggered
                if currentstate == 1 and previousstate == 0:
		
                    print("Motion detected!")
			
                    # Your IFTTT URL with event name, key and json parameters (values)
		    r = requests.post('https://maker.ifttt.com/trigger/motion_detected/with/key/cZhUuWri2gFkwEYnGWV1pRKM5N_ms97M_kEUxNRuoL_', params={"value1":"none","value2":"none","value3":"none"})
			
		    # Record new previous state
		    previousstate = 1
			
		    #Wait 120 seconds before looping again
		    print("Waiting 120 seconds")
		    time.sleep(120)
			
		# If the PIR has returned to ready state
		elif currentstate == 0 and previousstate == 1:
		
			print("Ready")
			previousstate = 0

		# Wait for 10 milliseconds
		time.sleep(0.01)"""

       

except KeyboardInterrupt:
	print("    Quit")

	# Reset GPIO settings
	GPIO.cleanup()
