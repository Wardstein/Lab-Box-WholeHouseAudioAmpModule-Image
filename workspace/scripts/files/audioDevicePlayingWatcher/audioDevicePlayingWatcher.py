#!/usr/bin/python

# This script watches the (default) alsa soundcard for its playing status to switch on or off an audio amplifier.
# It belongs to the https://github.com/Wardstein/Lab-Box-WholeHouseAudioAmpModule-Image of the https://github.com/Wardstein/Lab-Box project.
# The configured pins for the power enable and mute signals are the ones used on the Whole House Audio Amplifier module
# which can be found here: https://github.com/Wardstein/Lab-Box/Modules/Whole%20House%20Audio%20Amp


import sys
import time
import glob
from gpiozero import LED		# This package is installed by default on any raspberry pi OS image


# Config
powerOffAmpAdditionalToMute = True


# Few constants
AMP_POWER_GPIO = 6
MUTE_GPIO = 10


# Search for all possible cards and status files, but just take the first, as we should have only one anyways (I hope :D)
cardStati = glob.glob('/proc/asound/card*/pcm*p/sub*/status')
cardStatusFile = cardStati[0]
print("Using card status file: ", cardStatusFile)


def main():
        ampPowerGpio = LED(AMP_POWER_GPIO)
        ampPowerGpio.on()                                               # Switch amp on at startup
        muteGpio = LED(MUTE_GPIO)
        muteGpio.off()                                                  # But mute amp at startup

        while True:
                try:
                        f = open(cardStatusFile, 'r')
                        content = f.read()
                        f.close()
                        content = content.strip()
                        if content != "closed":
                                # print("Playing")
                                ampPowerGpio.on()                       # Power enable is high active
                                time.sleep(1)
                                muteGpio.on()                           # Mute on TAS5766 is low active
                        else:
                                # print("Closed")
                                muteGpio.off()                          # Mute on TAS5766 is low active
                                time.sleep(1)
                                if powerOffAmpAdditionalToMute == True:
                                        ampPowerGpio.off()              # Power enable is high active
                except:
                        pass

                time.sleep(1)


if __name__ == '__main__':
        try:
                main()
        except KeyboardInterrupt:
                print >> sys.stderr, '\nExiting by user request.\n'
                sys.exit(0)
