## About

transfero is a program the purpose of which to unite MTP FUSE filesystems
such as go-mtpfs, jmtpfs, mtpfs into one place and use it with friendly GUI interface.
The program allows you to transfer files between android devices and your local linux machine
via USB by using one or more FUSE filesystems at the same time. The GUI implementation almost
entirely relies on the next works:
* [go-mtpfs](https://github.com/hanwen/go-mtpfs)
* [jmtpfs](https://github.com/kiorky/jmtpfs)
* [mtpfs](https://github.com/cjd/mtpfs)

## Requirements
In order for the program to work properly you need to install **mtp-tools** and **PyQt5**. You can do that
by executing the next command:
```
sudo apt-get install mtp-tools
```
To install **PyQt5**

```
sudo apt-get install python3-pyqt5
```

> **Note:** For correct work, the program also requires **libmtp** to be installed but since **mtp-tools**
> already contains this library it's not necessary to install it apart

### If you want to use **go-mtpfs**
 You need to install **the Go compiler** and **go-mtpfs** itself

 To install the Go compiler
```
sudo apt-get install golang-go
```

To install go-mtpfs
```
sudo apt-get install go-mtpfs
```
### If you want to use **jmtpfs**
 You need to install **jmtpfs**

 To install jmtpfs
 ```
 sudo apt-get install jmtpfs
 ```
### If you want to use **mtpfs**
You need to install **mtpfs**

To install mtpfs
```
sudo apt-get install mtpfs
```

> **Note:** You should install all these libraries. If one of them doesn't work you can always use another one
## Install
### PPA
In order to install the program just type in the next commands:
```
sudo add-apt-repository ppa:jerichofs/jaconda
sudo apt-get update
sudo apt-get install transfero
```
## Guide
* Install all requirements
* connect your android device to the computer via USB
* Mount one of the filesystems **go-mtpfs**, **jmtpfs**, **mtpfs**
* in the Tree View in the Android folder you will see your mounted Android storage
* Share files (you can use key arrows left and right on you keyboard to transfer files)

> **Note:** All these libraries **does not work properly when the phone is locked by the lockscreen**
> (especially during transfering files). Unlock the phone and it should work again as long as
> the cord remains connected.