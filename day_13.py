package_pool = [4.8, 7.2, 14.4, 18.0, 22.5]

is_premium_tier = lambda n: n >= 15

premium_shortlist = list(filter(is_premium_tier, package_pool))

if __name__ == "__main__":
    print(f"All Packages: {package_pool}\nShortlist Packages: {premium_shortlist}")
    