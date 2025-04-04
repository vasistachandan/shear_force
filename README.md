# 📐 Moving Load Analysis for Simply Supported Beam

![Beam Analysis Illustration](docs/beam_analysis_illustration.png)

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

## Then follow the interactive prompts

Enter beam length L (m): 10./
Enter first load W1 (kN): 30./
Enter second load W2 (kN): 20./
Enter distance between loads x (m): 3./

