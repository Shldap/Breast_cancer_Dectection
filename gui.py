import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class TumorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tumor Image Viewer")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.on_drag)

        self.classify_button = tk.Button(self.root, text="Classify", command=self.classify_tumor)
        self.classify_button.pack()

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()

        self.classifier = None
        self.scaler = None

    def on_drag(self, event):
        x, y = event.x, event.y
        data = event.data

        if isinstance(data, str) and data.endswith(".png"):
            self.display_image(data, x, y)

    def display_image(self, image_path, x, y):
        image = Image.open(image_path)
        image.thumbnail((100, 100))  # Adjust the size as needed

        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(x, y, image=photo, tags="image")
        self.canvas.image = photo

    def classify_tumor(self):
        items = self.canvas.find_withtag("image")
        if not items:
            messagebox.showinfo("Error", "No image found on the canvas.")
            return
        
        image_item = items[-1]  # Get the latest added image
        image = self.canvas.itemcget(image_item, "image")
        image_path = image[5:-1]  # Remove the "pyimage" prefix and trailing parentheses

        if self.classifier is None or self.scaler is None:
            messagebox.showinfo("Error", "Classifier and scaler not initialized.")
            return

        # Load and preprocess the tumor image
        # Preprocess the image as needed (e.g., resize, convert to numerical representation)
        processed_image = preprocess_image(image_path)

        # Scale the features using the scaler
        scaled_features = self.scaler.transform(processed_image)

        # Perform tumor classification using the classifier
        prediction = self.classifier.predict(scaled_features)

        # Convert the prediction to a meaningful result
        classification_result = "Malignant" if prediction == 1 else "Benign"

        messagebox.showinfo("Tumor Classification", f"The tumor is classified as {classification_result}.")

    def clear_canvas(self):
        self.canvas.delete("image")

    def open_file(self):
        filetypes = (("PNG Images", "*.png"), ("All Files", "*.*"))
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=filetypes)
        if file_path:
            self.display_image(file_path, 200, 200)

if __name__ == "__main__":
    # Load and preprocess your dataset
    X, y = load_dataset()  # Replace with your own dataset loading code
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features using a scaler
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Create and train the Random Forest classifier
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(X_train, y_train)

    root = tk.Tk()
    app = TumorGUI(root)
    app.classifier = classifier
    app.scaler = scaler
    root.mainloop()
