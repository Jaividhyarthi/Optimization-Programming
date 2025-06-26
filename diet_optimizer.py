# task4_diet_optimizer.py

from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpStatus, value

# Step 1: Problem setup
model = LpProblem("Diet Optimization", LpMinimize)

# Step 2: Define food items with cost and nutrients (per unit)
foods = {
    'Chicken Breast': {'cost': 50, 'protein': 30, 'fat': 3, 'carbs': 0},
    'Brown Rice': {'cost': 20, 'protein': 3, 'fat': 1, 'carbs': 22},
    'Broccoli': {'cost': 10, 'protein': 2, 'fat': 0, 'carbs': 5},
    'Milk': {'cost': 15, 'protein': 8, 'fat': 5, 'carbs': 12},
}

# Step 3: Decision variables – how much of each food to eat
food_vars = {f: LpVariable(f.replace(" ", "_"), lowBound=0, cat='Continuous') for f in foods}

# Step 4: Objective – minimize total cost
model += lpSum(food_vars[f] * foods[f]['cost'] for f in foods), "Total Cost"

# Step 5: Nutritional constraints
# Require: ≥ 50g protein, ≤ 70g fat, ≥ 100g carbs

model += lpSum(food_vars[f] * foods[f]['protein'] for f in foods) >= 50, "ProteinRequirement"
model += lpSum(food_vars[f] * foods[f]['fat'] for f in foods) <= 70, "FatLimit"
model += lpSum(food_vars[f] * foods[f]['carbs'] for f in foods) >= 100, "CarbRequirement"

# Step 6: Solve
model.solve()

# Step 7: Print Results
print(f"📊 Status: {LpStatus[model.status]}")
print("🍽️ Recommended daily food intake:")

for f in foods:
    qty = food_vars[f].varValue
    if qty and qty > 0:
        print(f"  - {f}: {qty:.2f} units")

print(f"\n💰 Minimum total cost: ₹{value(model.objective):.2f}")
