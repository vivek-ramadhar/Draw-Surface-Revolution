# Surface of Revolution Generator

## Overview
This interactive application allows users to draw arbitrary curves that are then transformed into 3D surfaces of revolution. The app provides a simple drawing interface where users draw a "half-curve" which is then rotated around an axis to generate a complete 3D model.

## Features
- **Interactive Drawing Interface**: Simple and intuitive canvas for freehand curve creation
- **Real-time Visualization**: Instantly see your 2D curve alongside its 3D surface of revolution
- **Mathematical Modeling**: Demonstrates principles of parametric surfaces and computational geometry
- **Moment of Inertia Calculation**: Includes functions to calculate the moment of inertia tensor for the generated surface

## Technology Stack
- **Python**: Core programming language
- **Tkinter**: GUI framework for the drawing interface
- **Matplotlib**: 3D visualization of the generated surfaces
- **NumPy**: Mathematical computations and array manipulations

## How It Works
1. The user draws a curve on a canvas using mouse movements
2. When the "Generate Surface" button is clicked, the application:
   - Records the coordinates of the drawn curve
   - Uses parametric equations to revolve the curve around the y-axis
   - Displays both the original 2D curve and the resulting 3D surface

## Mathematical Foundation
The application uses parametric equations to generate the surface of revolution:
- For each point (x,y) on the original curve:
  - A circle is generated in the 3D space with radius x
  - The circle is positioned at height y
  - This creates a continuous surface when all circles are combined

## Usage
1. Run `surface-rev.py` to launch the application
2. Draw a curve using your mouse (the y-axis is vertical on the screen)
3. Click "Generate Surface" to see the 3D visualization
4. Close the visualization window to draw another curve

## Example Outputs
![Vase Example](https://github.com/vivek-ramadhar/Draw-Surface-Revolution/assets/47376625/a4dc84c9-5f42-4ab2-976f-d0f15291f068)
![3D Vase Visualization](https://github.com/vivek-ramadhar/Draw-Surface-Revolution/assets/47376625/1a138723-c856-4b13-984e-0d81fa1c1985)

![Bell Curve Example](https://github.com/vivek-ramadhar/Draw-Surface-Revolution/assets/47376625/6652fdf5-97a7-4861-895b-c2dbece4d4cc)
![3D Bell Visualization](https://github.com/vivek-ramadhar/Draw-Surface-Revolution/assets/47376625/a835cfd4-a7ed-4cf4-a657-3cb26c680ca5)

## Future Improvements
- Option to choose different axes of revolution
- Export capabilities for 3D models in standard formats (OBJ, STL)
- Enhanced drawing tools for more precise curve creation
- Texture and material mapping for more realistic visualizations

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/surface-revolution.git

# Navigate to the project directory
cd surface-revolution

# Install required dependencies
pip install matplotlib numpy

# Run the application
python surface-rev.py
```

## Requirements
- Python 3.6+
- NumPy
- Matplotlib
- Tkinter (usually included with Python)
