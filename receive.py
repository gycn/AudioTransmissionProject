import numpy as np
import scipy.signal

CARRIER_FREQUENCY_HIGH = 5e4
CARRIER_FREQUENCY_LOW = 4.5e4

CARRIER_FILTER_HALF_SPACE = 15

INPUT_SAMPLE_RATE = 1e6

WINDOW_FILTER_RESOLUTION = 511

ENVELOPE_RESOLUTION = 127

DATA_RATE = 100

WIND_FIR_LOW = scipy.signal.firwin(WINDOW_FILTER_RESOLUTION, 
                                    [(CARRIER_FREQUENCY_LOW - CARRIER_FILTER_HALF_SPACE) * 2/ INPUT_SAMPLE_RATE, 
                                     (CARRIER_FREQUENCY_LOW - CARRIER_FILTER_HALF_SAPCE) * 2/ INPUT_SAMPLE_RATE], pass_zero=False)

WIND_FIR_HIGH = scipy.signal.firwin(WINDOW_FILTER_RESOLUTION, 
                                    [(CARRIER_FREQUENCY_HIGH - CARRIER_FILTER_HALF_SPACE) * 2/ INPUT_SAMPLE_RATE, 
                                     (CARRIER_FREQUENCY_HIGH + CARRIER_FILTER_HALF_SPACE) * 2/ INPUT_SAMPLE_RATE], pass_zero=False)

ENVELOPE_COEFF = scipy.signal.firwin(ENVELOPE_RESOLUTION, DATA_RATE / INPUT_SAMPLE_RATE)

def bit_detection(input_data, start_sequence):
  low_filtered = np.abs(convolve(input_data, WIND_FIR_LOW))
  high_filtered = np.abs(convolve(input_data, WIND_FIR_LOW))
	
	envelope_low = convolve(low_filtered, low_pass_coeff)
	envelope_high = convolve(high_filtered, low_pass_coeff)
	
	recovered_data = envelope_high - envelope_low

	plt.figure()
	plt.plot(envelope_low)
	plt.plot(envelope_high)
	plt.plot(recovered_data)

	recovered_bits = [1]
	
	for bit in (recovered_data):
    if recovered_bits[-1] == 1 and bit < -0.01:
        recovered_bits.append(0)
    elif recovered_bits[-1] == 0 and bit > 0.01:
        recovered_bits.append(1)
    else:
        recovered_bits.append(recovered_bits[-1])
	
	plt.show()
	return recovered_bits
