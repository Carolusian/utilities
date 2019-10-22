# OnePlus 7Pro Android 10 Root Guidelines

* `cd platform-tools`
* `adb reboot bootloader`
* `./fastboot boot ../twrp-3.3.1-70-guacamole-unified-Q-mauronofrio.img`
* `Advanced` -> `ADB Sideload`
* `adb sideload ../twrp-3.3.1-70-guacamole-unified-installer-mauronofrio.zip`
* Install `Magisk`

## Ref:

* [[Guide] [Android 9/10] [7/7Pro] Unlock, TWRP, Root, and Update](https://forum.xda-developers.com/oneplus-7-pro/how-to/guide-bootloader-unlock-twrp-install-t3940368)
* [Fix fastboot error on MacOS](https://juzhax.com/2019/05/error-couldnt-create-a-device-interface-iterator-e00002bd/)
