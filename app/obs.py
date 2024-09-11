import obswebsocket
import cv2

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

	def start_virtual_cam(self):
		self.ws.call(obswebsocket.requests.StartVirtualCam())

	# def save_screenshot(self):
	# 	# Limpa os frames anteriores
	# 	limpar_frames()

	# 	self.start_recording()
	# 	sleep(0.1)
	# 	self.stop_recording()

	# 	while not glob('./frames/*'):
	# 		pass
	# 	sleep(0.25)

	# 	res = get_resolution(glob('./frames/*')[0])

	# 	# Salva o primeiro frame como imagem
	# 	save_first_frame(glob('./frames/*')[0], './frames/frame.png')

	# 	# Deleta o .mp4
	# 	limpar_frames("mp4")
	# 	limpar_frames("mkv")

	# 	return res

	def save_screenshot(self):

		# Limpar os frames anteriores
		limpar_frames()
		
		# Abrir a webcam (ID da webcam virtual do OBS pode variar, normalmente é 0 ou 1)
		cap = cv2.VideoCapture(1)  # Troque o índice para 1 se necessário

		# Definir a resolução para 1920x1080
		cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
		cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

		# Verificar se a captura foi aberta corretamente
		if not cap.isOpened():
			print("Erro ao acessar a webcam.")
			exit()

		# Ler um único frame da webcam
		ret, frame = cap.read()

		# Verificar se a leitura do frame foi bem-sucedida
		if not ret:
			print("Erro ao capturar o frame.")
		else:
			# Salvar o frame capturado como uma imagem
			cv2.imwrite('./frames/frame.png', frame)
			print("Frame salvo como 'frame.png'.")

		# Liberar o objeto de captura e fechar as janelas
		cap.release()
		cv2.destroyAllWindows()

		res = get_resolution(glob('./frames/*.png')[0])

		return res


