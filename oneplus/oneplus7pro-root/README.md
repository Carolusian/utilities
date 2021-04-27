# OnePlus 7Pro Android 10 Root Guidelines

## Why to root

Because Titanium is still the best way to back your phone. OnePlus switch's backup function still cause data loss.

## How to root

- `cd platform-tools`
- `adb reboot bootloader`
- `./fastboot boot ../twrp-3.3.1-70-guacamole-unified-Q-mauronofrio.img`
- `Advanced` -> `ADB Sideload`
- `adb sideload ../twrp-3.3.1-70-guacamole-unified-installer-mauronofrio.zip`
- Install `Magisk`

## How to install OTA upgrade

- Download and Install
- Before reboot, open `Magisk Manager`, in `Downloads`, install `TWRP A/B Retention Script`

> be careful, this may fail, so it is better to backup and using adb to flash new ROMs

## How to install ROM using TWRP

This step is necessary when the above method failed, and you stuck in boot. Then you need to flash stock boot.img and `downgrade`.

- `adb push ~/Downloads/ROM.zip /sdcard/`
- Then using `TWRP` to install

> NOTE: in system the path is `/storage/emulated/0/`

## Ref:

- [[Guide] [Android 9/10] [7/7Pro] Unlock, TWRP, Root, and Update](https://forum.xda-developers.com/oneplus-7-pro/how-to/guide-bootloader-unlock-twrp-install-t3940368)
- [Fix fastboot error on MacOS](https://juzhax.com/2019/05/error-couldnt-create-a-device-interface-iterator-e00002bd/)
- [Magisk flash cause hang on boot](https://www.oneplusbbs.com/forum.php?mod=viewthread&tid=4405118)
- [Android 10 TWRP & Root](https://www.oneplusbbs.com/thread-4968944-1.html)
