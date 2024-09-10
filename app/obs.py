import obswebsocket

class OBS:
	def __init__(self, host, port, password):
		self.ws = obswebsocket.obsws(host, port, password)
		self.ws.connect()

	def __del__(self):
		self.ws.disconnect()

	def start_stream(self):
		self.ws.call(obswebsocket.requests.StartStreaming())

	def stop_stream(self):
		self.ws.call(obswebsocket.requests.StopStreaming())

	def start_recording(self):
		self.ws.call(obswebsocket.requests.StartRecording())

	def stop_recording(self):
		self.ws.call(obswebsocket.requests.StopRecording())



