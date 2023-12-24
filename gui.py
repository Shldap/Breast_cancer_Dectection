import tkinter as tk
from PIL import Image, ImageTk

class TumorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tumor Image Viewer")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.on_drag)

    def on_drag(self, event):
        x, y = event.x, event.y
        data = event.data

        if isinstance(data, str) and data.endswith(".png"):
            self.display_image(data, x, y)

    def display_image(self, image_path, x, y):
        image = Image.open(image_path)
        image.thumbnail((100, 100))  # Adjust the size as needed

        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(x, y, image=photo)
        self.canvas.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = TumorGUI(root)
    root.mainloop()
