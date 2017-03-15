HIGH_CARRIER

wind_fir_low = scipy.signal.firwin(511, [35.0 * 2/ mod_sample_rate, 65.0  * 2/ mod_sample_rate], pass_zero=False)
wind_fir_high = scipy.signal.firwin(511, [135.0  * 2/ mod_sample_rate, 165.0  * 2/ mod_sample_rate], pass_zero=False)

low_pass_coeff = scipy.signal.firwin(127, bit_rate / mod_sample_rate)
