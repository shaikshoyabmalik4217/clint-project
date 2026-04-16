def calculate_alite(CaO, SiO2, Al2O3, Fe2O3):
    """
    Bogue's formula for Alite (C3S)
    Inputs are oxide percentages by mass
    """
    C3S = (4.071 * CaO) - (7.602 * SiO2) - (1.429 * Fe2O3) - (6.718 * Al2O3)
    return max(C3S, 0)  # prevents negative values


# Example input (typical clinker composition)
CaO = 65.0
SiO2 = 21.0
Al2O3 = 5.0
Fe2O3 = 3.0

alite = calculate_alite(CaO, SiO2, Al2O3, Fe2O3)
print(f"Estimated Alite (C3S) content: {alite:.2f}%")