# **OCR and Translation with OBS**

This project is a Python application that uses OCR (Optical Character Recognition) and machine translation to superimpose real-time translations onto videos, integrating with OBS Studio.
The application captures frames from a video, processes the found text, and adds the translation directly onto the image in OBS.

Observations: The application is not yet capable of identifying and translating in real-time. The processing time is very high and heavily depends on the hardware on which the application is running.
If you have optimization suggestions for the application, feel free to fork and submit a pull request.

Note 1: After installing NVIDIA CUDA drivers and installing PyTorch with CUDA enabled, performance improved significantly, taking only 5 seconds to generate.
Setup: RTX 3060 TI, I5-11400F, 16GB RAM 3200MHz

https://pytorch.org/get-started/locally/

## **Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Dependencies](#dependencies)
- [Contribution](#contribution)
- [License](#license)

## **Installation**

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/legulaas/OBS-Live-Translator.git](https://github.com/legulaas/OBS-Live-Translator.git)
    ```

2. **Install dependencies:**

    Create a virtual environment and install the necessary libraries:

    ```bash
    cd your_repository
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

    OBS WebSocket extension for OBS:
       https://github.com/obsproject/obs-websocket/releases

    Ensure that OBS Studio is installed and configured to accept WebSocket connections.

## **Usage**

1. **Configure OBS Studio:**
    - Make sure the OBS WebSocket plugin is installed and active.
    - Adjust the host, port, and password in the code to match your OBS settings.
    - Create an IMAGE source and select an image named "overlay.png" in the root of the repository (Even if it doesn't exist yet, as this will be the updated image with all translations applied).
    - In the `width` and `height` variables in the `main.py` file, set your OBS recording resolution.

2. **Run the script:**

    ```bash
    python main.py
    ```

3. **Keyboard control:**
    - **Scroll Lock:** Starts capturing and processing the current frame.
    - **Pause:** Clears captured frames and the overlay.
    - **F12:** Terminates the program.

## **Architecture**

- **WebSocket OBS:** Connects to and controls OBS Studio. (Some stream start functions are configured but not yet used; use as desired)
- **Frame Capture:** Saves the first captured video frame.
- **OCR and Translation:** Uses OCR to extract text and translates it to the desired language.
- **Overlay:** Adds the translated text onto the original image.
- **Logs:** Records events and errors for monitoring and debugging.

## **Dependencies**
- `easyocr`
- `deep_translator`
- `obs-websocket-py`
- `pandas`
- `opencv-python`
- `Pillow`
- `pynput`
- `glob`
- `app.ocr` (custom module for OCR)
- `app.translation` (custom module for translation)
- `app.overlay` (custom module for overlay)
- `app.log` (custom module for logs)
- `app.obs` (custom module for OBS integration)

To install the dependencies, use:

```bash
pip install -r requirements.txt
