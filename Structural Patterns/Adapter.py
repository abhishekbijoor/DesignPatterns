# 🔹 Imagine you have a USB keyboard (send_keystrokes()) but need to make it work with a Bluetooth device (transmit_data()).
# 🔹 Implement an Adapter to make them compatible.
from abc import ABC,abstractmethod

class USBKeyBoard:
    def __init__(self,type,language):
        print(f"class name : {__name__}")
        self.type = type
        self.language = language
        self.alphabets = []
    
    def send_keystrokes(self, alphabet):
        self.alphabets.append(alphabet)


class BluetoothDevice:
    def transmit_data(self,data):
        pass

class BluetoothAdapter(BluetoothDevice):
    def __init__(self,usbdevice:USBKeyBoard):
        super().__init__()
        self.usbdevice = usbdevice

    def transmit_data(self, data):
        print(f"class name : {__name__}")

        self.usbdevice.send_keystrokes(data)
        print(self.usbdevice.alphabets)

if __name__== "__main__":
    usbdevice = USBKeyBoard("USB","English")
    bluetoothAdapter = BluetoothAdapter(usbdevice)

    bluetoothAdapter.transmit_data("abc")
    bluetoothAdapter.transmit_data("cde")
