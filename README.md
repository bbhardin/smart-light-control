# smart-light-control

A small program using Webhooks and IFTTT to control my LIFX smart lights using my Raspberry Pi. Using the GPIO pins on the pi, I connected a broken window switch module from of my friend's 2001 Mercedes ML320 to allow for use as light switches. The top left switch turns on/off my left desk lamp and the top right switch turns on/off my right desk lamp. The switches on the bottom turn up and down the brightness of the lights depending on which light is selected from the passenger window lock toggle.

![Image of control board](https://github.com/bbhardin/smart-light-control/blob/master/IMG_8427.jpg)

Unfortunately, I was not able to determine between the up and down motion of the buttons. The computer relys on a difference in resistance to determine whether the button is pressed up or down. Using only digital inputs, I can not differentiate between up and down motion without a separate chip. That may come in a future iteration of the project.
