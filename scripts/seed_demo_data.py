#!/usr/bin/env python3
"""Placeholder demo data seeding script — implement per portfolio project."""

from __future__ import annotations

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed demo data into Chroma or local stores (template placeholder)."
    )
    parser.add_argument(
        "--data-dir",
        default="demo-data",
        help="Directory containing synthetic demo files (default: demo-data)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without writing data",
    )
    args = parser.parse_args()

    print("Cyber AI Project Template — seed_demo_data.py")
    print(f"  data_dir: {args.data_dir}")
    print(f"  dry_run:  {args.dry_run}")
    print()
    print("This is a placeholder. When copying the template for a portfolio project:")
    print("  1. Add synthetic files under demo-data/")
    print("  2. Implement chunking, embedding (nomic-embed-text), and Chroma upsert")
    print("  3. Document schemas in docs/demo-data.md")
    print()
    print("No data was written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
