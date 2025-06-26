# 📦 Task 4 – Optimization Problem using Linear Programming (PuLP)

This repository contains Task 4 of my Data Science Internship at CODTECH.

In this task, I modeled and solved a real-world **Linear Programming problem** using the Python library **PuLP** to demonstrate practical decision-making through optimization.

---

## 🎯 Problem Statement: Diet Optimization

> A person wants to plan a daily diet that **minimizes total cost** while ensuring they meet **nutritional requirements** such as protein, fat, and carbohydrates. The goal is to determine the optimal quantity of selected food items to consume.

---

## 🛠️ Tools & Libraries Used

- Python
- [PuLP](https://pypi.org/project/PuLP/) (LP modeling)
- NumPy (optional for calculations)

---

## 🔢 Input Data

| Food Item       | Cost ₹/unit | Protein (g) | Fat (g) | Carbs (g) |
|------------------|-------------|-------------|---------|-----------|
| Chicken Breast   | 50          | 30          | 3       | 0         |
| Brown Rice       | 20          | 3           | 1       | 22        |
| Broccoli         | 10          | 2           | 0       | 5         |
| Milk             | 15          | 8           | 5       | 12        |

---

## 🧠 Constraints

The minimum and maximum nutritional goals are:

- **Protein ≥ 50g**
- **Fat ≤ 70g**
- **Carbohydrates ≥ 100g**

---

## 🧮 Model Components

- **Decision Variables:** Quantity of each food to consume (continuous values)
- **Objective Function:** Minimize total cost  
  `Total Cost = ∑ (quantity × cost)`
- **Constraints:** Ensure nutritional requirements are met

---

## 🚀 How to Run the Code

1. Clone this repo or download the script
2. Make sure Python is installed
3. Install PuLP (if not already):
```bash
pip install pulp
Task 4 - Optimization Problem/
├── task4_diet_optimizer.py
├── README.md
