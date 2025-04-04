# 📐 Moving Load Analysis for Simply Supported Beam

This Python project performs **moving load analysis** on a **simply supported beam** using the **Influence Line Diagram** concept. It calculates maximum reactions at supports, shear forces, and bending moments under two moving point loads.

## 📊 Features

- Computes maximum:
  - Reaction forces at supports A and B
  - Shear force along the beam
  - Bending moment along the beam
- Plots Influence Lines for:
  - Reactions at A and B
  - Shear force at mid-span
  - Bending moment at mid-span
- Interactive CLI input
- Visual graphs using `matplotlib`

## 📦 Installation

First, clone the repository or download the Python script.

Install required dependencies:
```bash
pip install numpy matplotlib
```

## ▶️ How to Use
Run the Python file using any terminal or command prompt:
```bash
python beam_analysis.py
```

## 🧾 Then Follow the Interactive Prompts


Enter beam length L (m): 10<br>
Enter first load W1 (kN): 30<br>
Enter second load W2 (kN): 20<br>
Enter distance between loads x (m): 3<br>

## After entering the values, the analysis results will be shown.
## 📌 Sample Output

Results:<br>
Maximum Reaction at A: 33.00 kN (at W1 position = 0.00 m)<br>
Maximum Reaction at B: 33.00 kN (at W1 position = 10.00 m)<br>
Bending Moment BM_01 (W1 at 0 m): 0.00 kN·m<br>
Shear Force SF_01 (at 0.5L): -3.00 kN<br>
Maximum Shear Force SF_max: 33.00 kN (at position 0.00 m)<br>
Maximum Shear Force occurs when W1 is at position y = 0.00 m<br>
Maximum Bending Moment BM_max: 123.75 kN·m (at position 5.00 m)<br>
Maximum Bending Moment occurs when W1 is at position z = 4.79 m<br>

## 📈 Influence Line Plots
After the results are displayed, the script asks if you'd like to visualize the influence lines

Would you like to see influence line plots? (y/n): y

Once confirmed, the following plots are shown:

Influence Line for Reactions at A and B<br>
Influence Line for Shear Force at Mid-span<br>
Influence Line for Bending Moment at Mid-span<br>

## 🖼️ Example Plots
## Intensive line diagram
[![intensive-line-diagram.png](https://i.postimg.cc/NMDgSKwq/intensive-line-diagram.png)](https://postimg.cc/0M6RJ2Qc)

## 🧠 How It Works
This program simulates moving loads by shifting two point loads across a simply supported beam and computing:

Reactions using ILD (linear proportion based on position)  <br>
Shear Force and Bending Moment at each point  <br>
It uses a finely spaced numpy.linspace for smooth transitions and accurate peak detections  <br>


## 🛠️ Technologies Used

Python 🐍<br>
NumPy 📐<br>
Matplotlib 📊<br>

## 📚 Applications
Civil Engineering structural analysis  <br>  
Academic projects and assignments  <br>  
Understanding ILD behavior for beams  <br> 


## 🙋‍♂️ Author
Created by Chandan K Vasista

## 📄 License
MIT License - feel free to use and modify.


