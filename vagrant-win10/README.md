# Windows 10 VirtualBox VM Guest Quick Provisioning

## Usage

* Download the box already prepared
* `vagrant box add carolusian/windows10 windows10-vagrant.box`
* `vagrant up`
* Go to virtualbox GUI interface and input `vagrant`/`vagrant` as username and password
* Install chocolatey
* Install `adb`, run `cmd` in administrator mode: `choco install adb`
* Install VirtualBox Extension Pack to enable USB 3.0
* Install Guest Additions

## How to Prepare the Vagrant Box

### Install a VirtualBox VM

```
https://itsfoss.com/install-windows-10-virtualbox-linux/
```

### Export the VirtualBox VM to VagrantBox

```
https://huestones.co.uk/2015/08/creating-a-windows-10-base-box-for-vagrant-with-virtualbox/
https://softwaretester.info/create-windows-10-vagrant-base-box/
```
