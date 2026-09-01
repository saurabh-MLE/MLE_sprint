base_packages = [4, 6, 12, 15]

apply_bonus = lambda n: round(n*1.20, 2)

upgraded_packages = list(map(apply_bonus, base_packages))

if __name__ == "__main__":
    print(f"Packages before: {base_packages}\nPackages after Bonus: {upgraded_packages}")