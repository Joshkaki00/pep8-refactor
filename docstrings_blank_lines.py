"""Carbon monoxide monitoring device using onboard sensors."""
# by Kami Bigdely
# Docstrings and blank lines


class OnBoardTemperatureSensor:
    """Read temperature from the onboard voltage sensor."""

    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        """Initialize the onboard temperature sensor."""
        pass

    def read_voltage(self):
        """Return the current sensor voltage."""
        return 2.7

    def get_temperature(self):
        """Return the temperature in Celsius derived from voltage."""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR  # [celsius]


class CarbonMonoxideSensor:
    """Measure carbon monoxide level using voltage and temperature."""

    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        """Initialize with a temperature sensor, or create a default one."""
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Read voltage and return the computed carbon monoxide level."""
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = (
            CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(
                sensor_voltage,
                self.on_board_temp_sensor.get_temperature(),
            )
        )
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """Return the CO sensor voltage (simulated hardware reading)."""
        # In real life, it should read from hardware.
        return 2.3

    def convert_voltage_to_carbon_monoxide_level(voltage, temperature):
        """Convert sensor voltage and temperature into a CO level."""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature


class DisplayUnit:
    """Output messages to the console."""

    def __init__(self):
        """Initialize an empty display buffer."""
        self.string = ''

    def display(self, msg):
        """Print the given message."""
        print(msg)


class CarbonMonoxideDevice:
    """Combine a CO sensor and display unit to show readings."""

    def __init__(self, co_sensor, display_unit):
        """Store the sensor and display unit used by the device."""
        self.carbon_monoxide_sensor = co_sensor
        self.display_unit = display_unit

    def display(self):
        """Show the current carbon monoxide level on the display unit."""
        msg = (
            'Carbon Monoxide Level is : '
            + str(self.carbon_monoxide_sensor.get_carbon_monoxide_level())
        )
        self.display_unit.display(msg)


if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.display()
