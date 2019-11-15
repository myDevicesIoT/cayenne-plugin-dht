"""
This module provides a class for interfacing with DHT sensors.
"""
import os
import time

import Adafruit_DHT
from myDevices.utils.logger import info


class CayenneDHT():
    """Class for interacting with a DHT device"""

    def __init__(self, sensor, pin):
        """Initializes DHT device.

        Arguments:
        sensor: The sensor type, can be 11 or 22
        pin: The pin the DHT sensor is attached to
        """
        self.sensor = sensor
        self.pin = pin
        self.last_reading = 0
        self.humidity = None
        self.temperature = None

    def get_reading(self):
        """Gets the temperature and humidity readings from the sensor."""
        if self.last_reading + 2 < time.time():
            # Only take a new reading if a couple seconds have passed so if get_temperature and get_humidity
            # are called in succession they don't need to make two readings.
            self.humidity, self.temperature = Adafruit_DHT.read(self.sensor, self.pin)
            if self.humidity and self.temperature:
                self.last_reading = time.time()

    def get_temperature(self):
        """Gets the temperature as a tuple with type and unit."""
        self.get_reading()
        return (self.temperature, 'temp', 'c')

    def get_humidity(self):
        """Gets the humidity as a tuple with type and unit."""
        self.get_reading()
        return (self.humidity, 'rel_hum', 'p')
