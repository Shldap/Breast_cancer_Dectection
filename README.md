*not intended for medical use*This project is a tumor image classification application that uses a Random Forest classifier to predict whether a tumor is malignant or benign. The application provides a graphical user interface (GUI) where users can drag and drop tumor images for classification.

Features
Drag and drop tumor images onto the canvas for classification.
Uses a Random Forest classifier for tumor classification.
Displays the classification result (malignant or benign) in a message box.
Includes a clear button to remove the images from the canvas.
Supports preprocessing and scaling of the tumor images.
Installation
Clone the repository or download the project files.

Install the required dependencies by running the following command:

basic
Copy
pip install -r requirements.txt
```

Run the main script to start the application:

Copy
python main.py
```
Usage
Launch the application by running the main script.

The GUI window will open, showing an empty canvas.

To classify a tumor image, follow these steps:

Locate a tumor image on your computer.
Drag and drop the image onto the canvas.
The image will appear on the canvas.
Click the "Classify" button to perform tumor classification.
A message box will display the classification result.
To remove the images from the canvas, click the "Clear" button.

Customization
Dataset: Replace the load_dataset() function in main.py with your own code to load and preprocess your tumor image dataset.

Preprocessing: Adjust the preprocess_image() function in tumor_classification.py to preprocess the tumor images according to your requirements (e.g., resizing, conversion to numerical representation).

Hyperparameters: Modify the hyperparameters of the Random Forest classifier in tumor_classification.py based on your specific dataset and requirements.

GUI: Customize the GUI layout, appearance, and behavior by modifying the code in main.py.

Dependencies
Python 3.x
tkinter
scikit-learn
Pillow
License
This project is licensed under the MIT License.

Credits
Developed by Shlok dash
