#!/usr/bin/env python3
"""
Fibonacci Sequence
------------------
The Fibonacci sequence is a series of numbers where each number is the sum of
the two preceding ones, starting from 0 and 1.

  F(0) = 0
  F(1) = 1
  F(n) = F(n-1) + F(n-2)  for n >= 2

Fun fact: The ratio of consecutive Fibonacci numbers converges to the
Golden Ratio φ ≈ 1.6180339887…, a number found everywhere in nature —
from the spiral of a nautilus shell to the arrangement of sunflower seeds!
"""

import argparse
import math as _math

GOLDEN_RATIO = 1.6180339887


def fibonacci_sequence(n: int) -> list[int]:
    """Return a list containing the first n Fibonacci numbers (n >= 1)."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def golden_ratio_approx(sequence: list[int]) -> float:
    """Approximate the Golden Ratio using the last two Fibonacci numbers."""
    if len(sequence) < 2 or sequence[-2] == 0:
        return float("nan")
    return sequence[-1] / sequence[-2]


def fibonacci_spiral(sequence: list[int]) -> str:
    """
    Render a tiny ASCII art 'spiral' hinting at the Fibonacci / Golden-Ratio
    spiral found in nature.  Each row is padded to the width of the current
    Fibonacci number so the growing pattern is visible even in a terminal.
    """
    lines = []
    for i, value in enumerate(sequence):
        bar = "█" * min(value, 60)   # cap at 60 chars so the terminal doesn't explode
        lines.append(f"  F({i:>2}) = {value:>10}  {bar}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate the Fibonacci sequence and explore the Golden Ratio"
    )
    parser.add_argument(
        "-n",
        default=20,
        type=int,
        help="How many Fibonacci numbers to generate (default: 20)",
    )
    parser.add_argument(
        "--spiral",
        action="store_true",
        help="Print a visual bar chart hinting at the Fibonacci spiral",
    )
    args = parser.parse_args()

    if args.n <= 0:
        print("Please provide a positive integer for -n.")
        return

    sequence = fibonacci_sequence(args.n)

    print(f"\n🔢  First {args.n} Fibonacci numbers:")
    print("  " + ", ".join(str(v) for v in sequence))

    phi = golden_ratio_approx(sequence)
    if not _math.isnan(phi):
        print(f"\n✨  Golden Ratio approximation (F({args.n}) / F({args.n - 1})): {phi:.10f}")
        print(f"    True Golden Ratio φ ≈ {GOLDEN_RATIO}…")
        print(f"    Difference          : {abs(phi - GOLDEN_RATIO):.10f}")

    if args.spiral:
        print("\n📊  Fibonacci bar chart (each █ = 1 unit, capped at 60):")
        print(fibonacci_spiral(sequence))

    print()


if __name__ == "__main__":
    main()
