print("Script started")

from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus

print("PuLP imported successfully")

model = LpProblem(name="product-mix", sense=LpMaximize)

x = LpVariable(name="Product_A", lowBound=0)
y = LpVariable(name="Product_B", lowBound=0)

model += 40 * x + 50 * y, "Total_Profit"

model += (2 * x + 3 * y <= 100, "Labor_Constraint")
model += (3 * x + 2 * y <= 90, "Material_Constraint")

status = model.solve()

print(f"Solver Status: {LpStatus[model.status]}")

if LpStatus[model.status] == 'Optimal':
    print(f"Optimal Product A: {x.value():.2f}")
    print(f"Optimal Product B: {y.value():.2f}")
    print(f"Maximum Profit: ${value(model.objective):.2f}")
else:
    print("No optimal solution found.")
