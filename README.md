# Lab-Box Whole House Amplifier Raspberry Pi SD Card Image
This repo contains a pipeline to build the SD card image for the [Lab-Box Whole House Amplifier Module](https://github.com/Wardstein/Lab-Box/Modules/Whole%20House%20Audio%20Amp) Raspberry Pi.

Tasks this pipeline does:
* Update the base image
* ----Installs the boot config for the Raspberry Pi to use all the needed hardware of the Pi
* ---Modifies the base image with a new user, and other settings
* Installes snapclient software
* And finally cleans and packs the image

After you flashed an SD card and let the module/RasPi boot for the first time, it will go through multiple reboots until all stuff is set up. It will also stay still for a few minutes at some steps of the boot process, so don't worry. But this usually only takes five minutes (tested on a Raspberry Pi 2W).


# Flashing an SD card
Just download the latest image from the [release page of this repo here](https://github.com/Wardstein/Lab-Box-WholeHouseAudioAmpModule-Image/releases).

To flash an SD card, I can recommend using the [Raspberry Pi Imager](https://www.raspberrypi.com/software/). It can also apply WiFi settings such as SSID, password and country, and locale settings such as language and keyboard layout. BUT DO NOT SETUP A USER OR SSH SETTINGS, they are already done in the image!

Alternatively you can use [Balena Etcher](https://etcher.balena.io/), but it does not offer customizing any settings in the image.


# Missing


# Roadmap
* I would like to export a list of all installed packages with versions back to Github Actions and attach that file to the release to track the installed packages
	* But I could not figure out, how I pass something back from within CustoPiZer (chroot) to the Github Actions run environment
* Test building x64 images, here is a hint/fix how it should work: https://github.com/OctoPrint/CustoPiZer/issues/21
