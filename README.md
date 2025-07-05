# Polynomial Regression Calculator

This Python script provides a simple yet effective tool for performing polynomial regression on experimental data loaded from a CSV file. It allows you to model the relationship between two variables using a polynomial equation of a user-defined degree, visualize the experimental data, and compare it against the fitted regression model.

## Features

- **Data Loading**: Reads experimental data from a .csv file into a Pandas DataFrame.

- **Dynamic Polynomial Degree**: Allows the user to specify the degree of the polynomial for the regression model.

- **Coefficient Calculation**: Uses NumPy's linear algebra capabilities to efficiently calculate the polynomial coefficients.

- **Model Generation**: Constructs the polynomial regression model based on the calculated coefficients.

- **Visualization**: Plots the original experimental data points alongside the fitted polynomial regression curve using Matplotlib.

- **Extended Plotting Range**: Automatically extends the x-axis range slightly beyond the min/max of the experimental data for better visualization of the model's behavior.

## Requirements

To run this script, you need to have the following Python libraries installed:

- **numpy**

- **pandas**

- **matplotlib**

You can install them using pip:

```bash
pip install numpy pandas matplotlib

```

## How to Use

- Save the Script: Save the provided Python code as a .py file (e.g., linear_reg.py).

- Prepare Your Data: Ensure you have a CSV file named heat_capaacity_ethane.csv in the same directory as the script. The CSV file should contain two columns, with the first column representing the 'y' values (dependent variable) and the second column representing the 'x' values (independent variable).

- Run the Script: Open a terminal or command prompt, navigate to the directory where you saved the script and the CSV file, and run the script using Python:

```python
python linear_reg.py

```

- Enter Polynomial Degree: The script will prompt you to enter the desired degree for the polynomial model. Enter an integer (e.g., 1 for linear, 2 for quadratic, 3 for cubic, etc.) and press Enter.

- View the Plot: A Matplotlib plot will appear, displaying your experimental data points and the generated polynomial regression curve. The calculated coefficients will also be printed to the console.

## Code Overview

The script performs the following main steps:

- Imports: Imports numpy for numerical operations, pandas for data handling, and matplotlib.pyplot for plotting.

- Data Loading & Preprocessing:

- Loads data from heat_capaacity_ethane.csv into a Pandas DataFrame.

- Renames columns to "y" and "x" for clarity.

- Extracts 'y' and 'x' values into NumPy arrays.

- Calculates an extended X range using np.linspace for smoother plotting of the regression model.

- Matrix Construction (B):

- Constructs the design matrix B required for polynomial regression. For a polynomial of degree D, B will have columns corresponding to x^0 (ones), x^1, x^2, ..., x^D.

- Coefficient Calculation (sol):

- Applies the normal equation for linear least squares regression to find the optimal polynomial coefficients:


\mathbf{\beta} = (\mathbf{B}^T \mathbf{B})^{-1} \mathbf{B}^T \mathbf{y}


where \\mathbf{\\beta} is the vector of coefficients (sol), \\mathbf{B} is the design matrix, and \\mathbf{y} is the vector of dependent variables. np.linalg.solve is used for efficient and stable solution.

- The calculated coefficients are printed to the console.

- Model Prediction (Y):Uses the calculated coefficients (sol) and the extended X range to compute the predicted Y values for the regression curve.

- Plotting:

- Generates a scatter plot of the original experimental data points.

- Generates a line plot of the polynomial regression model.

- Adds a legend and displays the plot.

- This script provides a solid foundation for understanding and applying polynomial regression in Python.


**Please note that this readme was generated using AI**