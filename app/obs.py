import obswebsocket

from time import sleep
from glob import glob
from app.utils import save_first_frame, limpar_frames, get_resolution
from app.log import log

class OBS:
	def __init__(self, host, port, password):

		log(f'Iniciando OBS WebSocket com host {host}, porta {port} e senha {password}')

		self.ws = obswebsocket.obsws(host, port, password)
		self.ws.connect()

	def __del__(self):

		log('Desconectando OBS WebSocket')

		self.ws.disconnect()

	def start_stream(self):
		self.ws.call(obswebsocket.requests.StartStreaming())

	def stop_stream(self):
		self.ws.call(obswebsocket.requests.StopStreaming())

	def start_recording(self):
		self.ws.call(obswebsocket.requests.StartRecording())

	def stop_recording(self):
		self.ws.call(obswebsocket.requests.StopRecording())

	def save_screenshot(self):
		# Limpa os frames anteriores
		limpar_frames()

		self.start_recording()
		sleep(0.5)
		self.stop_recording()

		while not glob('./frames/*'):
			sleep(0.1)
		sleep(1)

		res = get_resolution(glob('./frames/*')[0])

		# Salva o primeiro frame como imagem
		save_first_frame(glob('./frames/*')[0], './frames/frame.png')

		# Deleta o .mp4
		limpar_frames("mp4")
		limpar_frames("mkv")

		return res



