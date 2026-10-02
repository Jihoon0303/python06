from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    heal = healing_potion()
    strength = strength_potion()
    print(f"Testing healing_potion: {heal}")
    print(f"Testing strength_potion: {strength}")


if __name__ == "__main__":
    main()