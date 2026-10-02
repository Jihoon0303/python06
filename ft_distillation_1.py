import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print(f"Using: 'import alchemy' structure to access potions")
    strength = alchemy.strength_potion()
    print(f"Testing strength_potion: {strength}")
    heal_alias = alchemy.heal()
    print(f"Testing heal alias: {heal_alias}")


if __name__ == "__main__":
    main()