
class MC34063():

    def __init__(
            self,
            output_voltage,
            output_voltage_tolerance,
            output_switching_frequency,
            output_current=1,
            input_voltage=5,
            output_ripple_voltage=0.1,
            set_resistor=10000
        ):
        self.output_voltage = output_voltage
        self.output_voltage_frequency = output_voltage_frequency
        self.output_switching_frequency = output_switching_frequency
        self.output_current = output_current
        self.input_voltage = input_voltage
        self.output_ripple_voltage = output_ripple_voltage
        self.set_resistor = set_resistor
        self._recalculate()

    def _recalculate(self):
        pass

    @property
    def output_voltage(self):
        return self.output_voltage

    @output_voltage.setter
    def output_voltage(self, output_voltage):
        self.output_voltage = output_voltage
        self._recalculate()

    @property
    def output_voltage_tolerance(self):
        return self.output_voltage_tolerance

    @output_voltage_tolerance.setter
    def output_voltage_tolerance(self, output_voltage_tolerance):
        self.output_voltage_tolerance = output_voltage_tolerance
        self._recalculate()

    @property
    def output_switching_frequency(self):
        return self.output_switching_frequency

    @output_switching_frequency.setter
    def output_switching_frequency(self, output_switching_frequency):
        self.output_switching_frequency = output_switching_frequency
        self._recalculate()

    @property
    def output_current(self):
        return self.output_current

    @output_current.setter
    def output_current(self, output_current):
        self.output_current = output_current
        self._recalculate()

    @property
    def input_voltage(self):
        return self.input_voltage

    @input_voltage.setter
    def input_voltage(self, input_voltage):
        self.input_voltage = input_voltage
        self._recalculate()

    @property
    def output_voltage_ripple(self):
        return self.output_voltage_ripple

    @output_voltage_ripple.setter
    def output_voltage_ripple(self, input_voltage):
        self.output_voltage_ripple = input_voltage
        self._recalculate()
        
    @property
    def set_resistor(self):
        return self.set_resistor

    @set_resistor.setter
    def set_resistor(self, input_voltage):
        self.set_resistor = input_voltage
        self._recalculate()

    @property
    def switching_ratio(self):
        return self.switching_ratio

    @property
    def switching_period(self):
        return self.switching_period

    @property
    def switching_on_time(self):
        return self.switching_on_time

    @property
    def switching_off_time(self):
        return self.switching_off_time

