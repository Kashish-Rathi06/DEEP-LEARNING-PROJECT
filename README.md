# DEEP-LEARNING-PROJECT
Company: CODTECH IT SOLUTIONS

NAME: Kashish Rathi

INTERN ID:CT06DH2160

DOMAIN:Data Science

DURACTION: 6 WEEKS

MENTOR: NEELA SANTOSH

📝 Script Description: Linear Programming for Product Mix Optimization Using PuLP

This Python script uses the PuLP library to solve a linear programming (LP) problem focused on optimizing a product mix. The main objective is to maximize profit by determining how many units of two products—Product A and Product B—should be produced, given limited resources such as labor and materials.

The script begins by printing a message to confirm that execution has started. It then imports essential components from the pulp package, including:

LpMaximize: Specifies the problem is a maximization task.

LpProblem: For defining the optimization model.

LpVariable: To create decision variables.

value and LpStatus: For retrieving results and status after solving.

Next, the script creates a linear programming model named "product-mix" with the goal of maximizing the objective function.

Two decision variables are defined:

x: Represents the number of units of Product A to produce.

y: Represents the number of units of Product B.

Both variables are constrained to be non-negative, as it doesn't make sense to produce negative quantities.

The objective function is defined as:

40 * x + 50 * y


This represents the total profit, where Product A yields $40 profit per unit, and Product B yields $50 per unit.

The script also defines two constraints:

Labor Constraint: 2x + 3y ≤ 100 (each unit of A uses 2 hours, B uses 3; total available is 100).

Material Constraint: 3x + 2y ≤ 90 (A uses 3 units, B uses 2; total material available is 90).

After setting up the model, it is solved using PuLP’s built-in solver. The script checks the solution status using LpStatus. If an optimal solution is found, it prints:

The optimal number of units to produce for Product A and B.

The maximum profit that can be achieved.

If no optimal solution is found, it notifies the user accordingly.

✅ Conclusion

This script is a practical example of how linear programming can be applied in business decision-making, especially in operations and resource management. By using PuLP, complex problems can be modeled and solved efficiently with just a few lines of Python code.

#OUTPUT

<img width="1913" height="1072" alt="Image" src="https://github.com/user-attachments/assets/a80ae7b2-d0fe-46b3-8224-4ba93e54cc3f" />
