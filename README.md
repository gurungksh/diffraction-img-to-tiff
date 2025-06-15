# img-to-tiff-exe Project

This project provides a simple GUI application for converting .img files to .tiff format. The application is built using Python and utilizes libraries such as NumPy and tifffile for image processing. It is primarily designed for scientific microscopy images, especially diffraction images commonly used in materials science and related fields.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Building the Executable](#building-the-executable)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. Clone the repository:

git clone <repository-url>
cd img-to-tiff-exe


2. Install the required dependencies:

pip install -r requirements.txt


## Usage

1. **Run the application:**

python src/smv_to_tiff.py


2. **Use the GUI** to configure your conversion:
- **Input Folder:** Select the folder that contains your `.img` files.
- **Output Folder:** Choose where to save the resulting `.tiff` files.
- **Width and Height:**  
  These define the **dimensions of the image** in pixels. Because `.img` files contain raw binary data without metadata, you must provide the correct image shape.  
  For example, if your image is 2048 pixels wide and 2048 pixels tall, enter:  
  - Width: `2048`  
  - Height: `2048`
- **Pixel Type (Bit Depth):**  
  This sets how the program interprets the values of each pixel in the binary file. You should choose the correct type based on how the `.img` files were saved.

  | Pixel Type | Bits per Pixel | Value Range             | Use Case                                      |
  |------------|----------------|--------------------------|-----------------------------------------------|
  | `uint8`    | 8              | 0 to 255                 | Simple grayscale images                       |
  | `uint16`   | 16             | 0 to 65,535              | Medical, microscopy, or scientific imaging    |
  | `float32`  | 32             | Any decimal number       | Scientific measurements, intensity maps       |

  **If you choose the wrong width, height, or pixel type,** the resulting images may look distorted, or conversion might fail.

3. **Click "Convert Files"** to start the conversion.  
A message will pop up showing how many files were successfully converted, and if any failed.

## Building the Executable

To build an executable from the project, you can use a packaging tool like PyInstaller. Follow these steps:

1. Install PyInstaller:

pip install pyinstaller


2. Navigate to the project directory and run:

pyinstaller --onefile src/smv_to_tiff.py


3. The executable will be created in the `dist` folder.

## Dependencies

- numpy
- tifffile
- tkinter

## License

This project is licensed under the MIT License. See the LICENSE file for details.

If you want, I can also help you generate a requirements.txt or example screenshots to make it even clearer!