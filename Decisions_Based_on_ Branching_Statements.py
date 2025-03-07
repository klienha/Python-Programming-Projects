def spectral_color(wavelength):
	result = 'initial value'
	if wavelength < 380:
		result = "ultraviolet"
	elif wavelength < 450:
		result = "violet"
	elif wavelength < 485:
		result = "blue"
	elif wavelength < 500:
		result = "cyan"
	elif wavelength < 565:
		result = "green"
	elif wavelength < 590:
		result = "yellow"
	elif wavelength < 625:
		result = "orange"
	elif wavelength < 750:
		result = "red"
	else:
		result = "infrared"
	return result

def robot_actions(side_sensor, front_sensor, dirt_sensor):
	result = 'initial value'
	if dirt_sensor == "dirt":
		result = "vacuum"
	elif side_sensor == "wall" and front_sensor == "clear":
		result = "forward"
	elif front_sensor == "wall":
		result = "turn"
	else:
		result = "stop"
	return result

def bad_broker(price, prev_price):
	result = 'initial value'
	pct_change = price/prev_price - 1.0
	if pct_change > 0.5:
		result = "BUY"
	elif pct_change < -0.5:
		result = "HOLD"
	else:
		result = "SELL"
	return result
