"""Validate or normalize an MCP capability inventory snapshot.

This script does not invent capabilities and does not connect to external systems.
Pass a JSON snapshot obtained from the authorized local MCP server with --input.
"""

import argparse
import json
from pathlib import Path


REQUIRED_KEYS = ("server", "tools", "resources", "prompts")


def load_inventory(path):
    with path.open(encoding="utf-8") as source:
        inventory = json.load(source)
    missing = [key for key in REQUIRED_KEYS if key not in inventory]
    if missing:
        raise ValueError(f"Missing inventory keys: {', '.join(missing)}")
    for key in ("tools", "resources", "prompts"):
        if not isinstance(inventory[key], list):
            raise ValueError(f"Inventory field {key} must be a list")
    return inventory


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("mcp_inventory.json"))
    parser.add_argument("--output", type=Path, default=Path("mcp_inventory.json"))
    args = parser.parse_args()
    inventory = load_inventory(args.input)
    with args.output.open("w", encoding="utf-8") as target:
        json.dump(inventory, target, indent=2)
        target.write("\n")
    print(f"Validated {len(inventory['tools'])} tools, "
          f"{len(inventory['resources'])} resources, "
          f"{len(inventory['prompts'])} prompts")


if __name__ == "__main__":
    main()