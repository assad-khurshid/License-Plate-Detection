
# Real-Time License Plate Detection

This project implements a real-time license plate detection system using advanced deep learning techniques. The system is designed to identify and read vehicle license plates from live video feeds or images, making it applicable in various fields such as traffic monitoring, parking management, and law enforcement.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Project Overview

This project leverages the YOLOv8 (You Only Look Once) model, which is renowned for its speed and accuracy in object detection tasks. The model is trained on a custom dataset to specifically detect license plates. The application is built with a user-friendly interface using Flask, allowing users to upload images or stream video for real-time detection.

![YOLOv8 Model Diagram](https://github.com/assad-khurshid/License-Plate-Detection/blob/main/Screenshot%202024-08-11%20110240.png)


## Features

- **Real-Time Detection**: Processes video feeds in real-time to detect and extract license plate information.
- **Custom Model Training**: Utilizes YOLOv8 with a custom dataset for highly accurate license plate detection.
- **Web Interface**: Simple and intuitive web interface powered by Flask.
- **Python 3.11 Compatibility**: The project is fully compatible with Python 3.11.

## Installation

### Prerequisites

- Python 3.11
- Anaconda3 Navigator
- Flask
- YOLOv8
- Virtual environment (optional but recommended)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/real-time-license-plate-detection.git
   cd real-time-license-plate-detection
   ```

2. **Set Up the Environment**:
   ```bash
   conda create --name license-plate-detection python=3.11
   conda activate license-plate-detection
   ```

3. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   flask run
   ```

## Usage

1. Access the web interface via `http://127.0.0.1:5000/`.
2. Upload an image or start a video feed.
3. View the detected license plates in real-time.

## Methodology

The project follows a systematic approach to build a robust license plate detection system:

### Basic Detection Model

The model is trained using the YOLOv8 algorithm, which includes pretrained weights. The custom dataset used for training enhances the model's ability to accurately detect license plates under various conditions.

Here’s a diagram illustrating the YOLOv8 model's working principle:

![YOLOv8 Model Diagram](https://github.com/assad-khurshid/License-Plate-Detection/blob/main/Screenshot%202024-08-11%20111051.png)

### User Interface

The web application interface is designed using Flask, providing an easy-to-use platform for users to interact with the detection system.

## Technologies Used

- **Anaconda3 Navigator**: Primary IDE for coding and debugging.
- **Python 3.11**: Programming language and interpreter.
- **Flask**: Framework for building the web interface.
- **YOLOv8**: The core object detection model used in the project.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
