import os
import numpy as np
import tifffile
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_all_img_to_tiff(input_folder, output_folder,
                            width=2048, height=2048,
                            dtype=np.uint16, header_size=512):
    os.makedirs(output_folder, exist_ok=True)

    converted = 0
    failed = []

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.img'):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.tiff'
            output_path = os.path.join(output_folder, output_filename)

            with open(input_path, 'rb') as f:
                f.seek(header_size)
                raw = f.read()

            try:
                image = np.frombuffer(raw, dtype=dtype).reshape((height, width))
                tifffile.imwrite(output_path, image)
                converted += 1
            except Exception as e:
                failed.append((filename, str(e)))

    return converted, failed

# GUI setup
def start_gui():
    def browse_input():
        path = filedialog.askdirectory()
        if path:
            input_var.set(path)

    def browse_output():
        path = filedialog.askdirectory()
        if path:
            output_var.set(path)

    def run_conversion():
        input_path = input_var.get()
        output_path = output_var.get()

        try:
            width = int(width_var.get())
            height = int(height_var.get())
            dtype = dtype_map[dtype_var.get()]
        except Exception:
            messagebox.showerror("Invalid input", "Width, height, or type is invalid.")
            return

        converted, failed = convert_all_img_to_tiff(
            input_folder=input_path,
            output_folder=output_path,
            width=width,
            height=height,
            dtype=dtype
        )

        msg = f"✅ Converted: {converted} file(s)."
        if failed:
            msg += f"\n❌ Failed: {len(failed)} file(s)."
        messagebox.showinfo("Done", msg)

    root = tk.Tk()
    root.title("IMG to TIFF Converter")

    input_var = tk.StringVar()
    output_var = tk.StringVar()
    width_var = tk.StringVar(value="2048")
    height_var = tk.StringVar(value="2048")
    dtype_var = tk.StringVar(value="uint16")
    dtype_map = {
        "uint8": np.uint8,
        "uint16": np.uint16,
        "float32": np.float32
    }

    tk.Label(root, text="Input Folder:").grid(row=0, column=0, sticky='e')
    tk.Entry(root, textvariable=input_var, width=40).grid(row=0, column=1)
    tk.Button(root, text="Browse", command=browse_input).grid(row=0, column=2)

    tk.Label(root, text="Output Folder:").grid(row=1, column=0, sticky='e')
    tk.Entry(root, textvariable=output_var, width=40).grid(row=1, column=1)
    tk.Button(root, text="Browse", command=browse_output).grid(row=1, column=2)

    tk.Label(root, text="Width:").grid(row=2, column=0, sticky='e')
    tk.Entry(root, textvariable=width_var, width=10).grid(row=2, column=1, sticky='w')

    tk.Label(root, text="Height:").grid(row=3, column=0, sticky='e')
    tk.Entry(root, textvariable=height_var, width=10).grid(row=3, column=1, sticky='w')

    tk.Label(root, text="Pixel Type:").grid(row=4, column=0, sticky='e')
    tk.OptionMenu(root, dtype_var, *dtype_map.keys()).grid(row=4, column=1, sticky='w')

    tk.Button(root, text="Convert Files", command=run_conversion, bg="lightgreen").grid(row=5, column=1, pady=10)

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    start_gui()