# Cayenne DHT Plugin
A plugin allowing the [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent) to read data from DHT11, DHT22 and AM2302 sensors and display it in the [Cayenne Dashboard](https://cayenne.mydevices.com).

## Requirements
### Hardware
* [Rasberry Pi](https://www.raspberrypi.org).
* [DHT11](https://www.adafruit.com/product/386), [DHT22](https://www.adafruit.com/product/385) or [AM2302](https://www.adafruit.com/product/393)

### Software
* [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent). This can be installed from the [Cayenne Dashboard](https://cayenne.mydevices.com).
* [Git](https://git-scm.com/).
* pip3 - Python 3 package manager. This should already be available in Python 3.4+ and above. If not it can be installed using the system package manager. Via apt-get this would be:
  ```
  sudo apt-get install python3-pip
  ```

## Getting Started
1. Installation
   From the command line run the following commands to install this plugin.
   ```
   cd /etc/myDevices/plugins
   sudo git clone https://github.com/myDevicesIoT/cayenne-plugin-dht.git
   cd cayenne-plugin-dht
   sudo pip3 install .
   ```

2. Setting the sensor type and pin
   Specify the sensor type and pin you are using by modifying `init_args` under `DHT Temperature` in the `cayenne-dht.plugin` file.
   For a DHT11 use `11` for the sensor argument, for a DHT22 use `22` and for a AM2302 use `2302`. Set the pin argument to the GPIO
   pin number your sensor is connected to. For example, a DHT11 on pin 17 would use the following:
   ```
   init_args={"sensor": 11, "pin": 17}
   ```

3. Restarting the agent
   Restart the agent so it can load the plugin.
   ```
   sudo service myDevices restart
   ```
