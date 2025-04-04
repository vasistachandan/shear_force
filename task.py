"""
Moving Load Analysis for Simply Supported Beam using Influence Line Diagram
Author: [Your Name]
Purpose: Calculate maximum reactions, shear forces, and bending moments for a simply supported beam
         subjected to moving loads using the influence line diagram concept.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict


def analyze_beam(L: float, W1: float, W2: float, x: float) -> Dict:
    """
    Analyze a simply supported beam subjected to two moving loads W1 and W2 separated by distance x.
    Uses influence line diagram concept to find maximum values and their locations.
    
    Args:
        L (float): Length of the beam in meters
        W1 (float): First moving load in kN
        W2 (float): Second moving load in kN
        x (float): Distance between W1 and W2 in meters
    
    Returns:
        Dict: Dictionary containing all required output values
    """
    # Input validation
    if L <= 0:
        raise ValueError("Beam length must be positive")
    if x < 0 or x > L:
        raise ValueError(f"Distance x must be between 0 and {L}")
    if W1 <= 0 or W2 <= 0:
        raise ValueError("Load values must be positive")
    
    # Create a fine division of the beam for analysis
    num_points = 1000
    positions = np.linspace(0, L, num_points)
    
    # Initialize arrays to store results for each position of the load system
    Ra_values = np.zeros(num_points)  # Reaction at support A
    Rb_values = np.zeros(num_points)  # Reaction at support B
    
    # Bending moment at each position for different load positions
    BM_values = np.zeros((num_points, num_points))
    
    # Shear force at each position for different load positions
    SF_values = np.zeros((num_points, num_points))
    
    # Position of W1 along the beam (y)
    for i, y in enumerate(positions):
        if y <= L:  # W1 is on the beam
            # Check if W2 is also on the beam
            if y + x <= L:
                # Both loads on the beam
                # Calculate reactions using influence line concept
                Ra_w1 = W1 * (L - y) / L
                Ra_w2 = W2 * (L - (y + x)) / L if y + x >= 0 else 0
                Ra = Ra_w1 + Ra_w2
                
                Rb_w1 = W1 * y / L
                Rb_w2 = W2 * (y + x) / L if y + x >= 0 else 0
                Rb = Rb_w1 + Rb_w2
            else:
                # Only W1 is on the beam
                Ra = W1 * (L - y) / L
                Rb = W1 * y / L
        else:
            # No loads on the beam
            Ra = 0
            Rb = 0
        
        Ra_values[i] = Ra
        Rb_values[i] = Rb
        
        # Calculate shear force and bending moment at each point along the beam
        for j, z in enumerate(positions):
            # Shear force calculation
            if z < y:
                # Point is before W1
                SF = Ra
            elif z == y:
                # Point is exactly at W1
                SF = Ra - W1/2  # Average value at discontinuity
            elif z < y + x and y + x <= L:
                # Point is between W1 and W2
                SF = Ra - W1
            elif z == y + x and y + x <= L:
                # Point is exactly at W2
                SF = Ra - W1 - W2/2  # Average value at discontinuity
            elif z > y + x and y + x <= L:
                # Point is after W2
                SF = Ra - W1 - W2
            else:
                # Point is after W1 (and W2 is not on the beam)
                SF = Ra - W1
            
            SF_values[i, j] = SF
            
            # Bending moment calculation using influence line concept
            if z < y:
                # Point is before W1
                BM = Ra * z
            elif z > y and z < y + x and y + x <= L:
                # Point is between W1 and W2
                BM = Ra * z - W1 * (z - y)
            elif z > y + x and y + x <= L:
                # Point is after W2
                BM = Ra * z - W1 * (z - y) - W2 * (z - (y + x))
            else:
                # Point is after W1 (and W2 is not on the beam)
                BM = Ra * z - W1 * (z - y)
            
            BM_values[i, j] = BM
    
    # Find maximum values and their locations
    max_Ra_index = np.argmax(Ra_values)
    max_Ra = Ra_values[max_Ra_index]
    max_Ra_position = positions[max_Ra_index]
    
    max_Rb_index = np.argmax(Rb_values)
    max_Rb = Rb_values[max_Rb_index]
    max_Rb_position = positions[max_Rb_index]
    
    # Find the position of W1 that gives maximum shear force and its location
    max_SF = -float('inf')
    max_SF_position = 0
    max_SF_w1_position = 0
    
    for i, y in enumerate(positions):
        max_index = np.argmax(np.abs(SF_values[i]))
        if abs(SF_values[i, max_index]) > abs(max_SF):
            max_SF = SF_values[i, max_index]
            max_SF_position = positions[max_index]
            max_SF_w1_position = y
    
    # Find the position of W1 that gives maximum bending moment and its location
    max_BM = -float('inf')
    max_BM_position = 0
    max_BM_w1_position = 0
    
    for i, y in enumerate(positions):
        max_index = np.argmax(BM_values[i])
        if BM_values[i, max_index] > max_BM:
            max_BM = BM_values[i, max_index]
            max_BM_position = positions[max_index]
            max_BM_w1_position = y
    
    # Calculate specific required values
    # BM_01: Bending moment when W1 is at 0 m
    BM_01_index = 0  # W1 at position 0
    BM_01 = BM_values[BM_01_index, 0]  # Bending moment at W1 position
    
    # SF_01: Shear force at 0.5L
    mid_point_index = np.argmin(np.abs(positions - 0.5 * L))
    SF_01 = SF_values[0, mid_point_index]  # Shear force at midpoint when W1 at 0
    
    # Prepare output dictionary
    results = {
        "max_reaction_A": max_Ra,
        "max_reaction_A_position": max_Ra_position,
        "max_reaction_B": max_Rb,
        "max_reaction_B_position": max_Rb_position,
        "BM_01": BM_01,
        "SF_01": SF_01,
        "max_SF": max_SF,
        "max_SF_position": max_SF_position,
        "max_SF_w1_position": max_SF_w1_position,
        "max_BM": max_BM,
        "max_BM_position": max_BM_position,
        "max_BM_w1_position": max_BM_w1_position
    }
    
    return results


def plot_influence_lines(L: float) -> None:
    """
    Plot influence lines for reactions, shear force, and bending moment
    for a simply supported beam.
    
    Args:
        L (float): Length of the beam in meters
    """
    positions = np.linspace(0, L, 100)
    
    # Influence line for reaction at A
    Ra_influence = (L - positions) / L
    
    # Influence line for reaction at B
    Rb_influence = positions / L
    
    # Influence line for shear force at mid-span
    SF_midspan_influence = np.zeros_like(positions)
    SF_midspan_influence[positions <= L/2] = -positions[positions <= L/2] / L
    SF_midspan_influence[positions > L/2] = -(L - positions[positions > L/2]) / L
    
    # Influence line for bending moment at mid-span
    BM_midspan_influence = np.zeros_like(positions)
    BM_midspan_influence = (positions * (L - positions)) / L
    
    # Plotting
    plt.figure(figsize=(12, 10))
    
    plt.subplot(3, 1, 1)
    plt.plot(positions, Ra_influence, 'b-', label='Reaction at A')
    plt.plot(positions, Rb_influence, 'r-', label='Reaction at B')
    plt.xlabel('Load Position (m)')
    plt.ylabel('Influence Value')
    plt.title('Influence Lines for Reactions')
    plt.grid(True)
    plt.legend()
    
    plt.subplot(3, 1, 2)
    plt.plot(positions, SF_midspan_influence, 'g-')
    plt.xlabel('Load Position (m)')
    plt.ylabel('Influence Value')
    plt.title('Influence Line for Shear Force at Mid-span')
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    plt.plot(positions, BM_midspan_influence, 'm-')
    plt.xlabel('Load Position (m)')
    plt.ylabel('Influence Value')
    plt.title('Influence Line for Bending Moment at Mid-span')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to take user inputs and display results.
    """
    print("Moving Load Analysis for Simply Supported Beam")
    print("=============================================")
    
    # Get user inputs
    try:
        L = float(input("Enter beam length L (m): "))
        W1 = float(input("Enter first load W1 (kN): "))
        W2 = float(input("Enter second load W2 (kN): "))
        x = float(input("Enter distance between loads x (m): "))
        
        # Analyze the beam
        results = analyze_beam(L, W1, W2, x)
        
        # Display results
        print("\nResults:")
        print(f"Maximum Reaction at A: {results['max_reaction_A']:.2f} kN (at W1 position = {results['max_reaction_A_position']:.2f} m)")
        print(f"Maximum Reaction at B: {results['max_reaction_B']:.2f} kN (at W1 position = {results['max_reaction_B_position']:.2f} m)")
        print(f"Bending Moment BM_01 (W1 at 0 m): {results['BM_01']:.2f} kN·m")
        print(f"Shear Force SF_01 (at 0.5L): {results['SF_01']:.2f} kN")
        print(f"Maximum Shear Force SF_max: {results['max_SF']:.2f} kN (at position {results['max_SF_position']:.2f} m)")
        print(f"Maximum Shear Force occurs when W1 is at position y = {results['max_SF_w1_position']:.2f} m")
        print(f"Maximum Bending Moment BM_max: {results['max_BM']:.2f} kN·m (at position {results['max_BM_position']:.2f} m)")
        print(f"Maximum Bending Moment occurs when W1 is at position z = {results['max_BM_w1_position']:.2f} m")
        
        # Ask user if they want to see influence line plots
        see_plots = input("\nWould you like to see influence line plots? (y/n): ")
        if see_plots.lower() == 'y':
            plot_influence_lines(L)
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()