# AI Calculator

aicalculator is a unique application that leverages machine learning and computer vision to enable users to solve mathematical problems by simply drawing them with their hands. 
The project uses OpenCV for image processing and the Gemini model for powerful problem-solving capabilities.

## Features

* Intuitive Interface: A visually appealing OpenCV-based interface that guides users through the drawing process.
* Handwritten Equation Recognition: Uses computer vision techniques to accurately recognize handwritten mathematical equations.
* Real-time Drawing: Allows users to draw directly on the screen using their mouse.
* Problem Solving: Sends drawn images to the Gemini model for analysis and solution generation.
* Clear and Send Commands: Simple mouse gestures for clearing the drawing area and submitting the image for processing.

   * Hold $${\color{red}Mouse LBUTTON}$$ down to draw.
   * Double click $${\color{yellow}Mouse LBUTTON}$$ to clear screen.
   * Click $${\color{orange}Mouse RBUTTON}$$ to get results.
 
## Usage

1. Clone this repo using

   ```
     git clone https://github.com/umerfar123/AI-Calculator.git
   ```
2. Install required libraries using

   ```python
    pip install opencv-python
   ```
   ```python
    pip install -q -U google-generativeai
   ```
3. Create your own api key for gemini model and paste it in apikey variable.

   ```
     apk = 'your api key'
   ```
4. Run the main file

   ```python
    python main.py
   ```
## Demo

https://github.com/user-attachments/assets/3403f345-f97d-414c-935f-b43fb4bb3558

## Contributions
Contributions to this project are welcome! Feel free to fork the repository, make changes, and submit a pull request.
