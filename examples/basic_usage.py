#!/usr/bin/env python3
"""Basic usage example for bvh_motion_tools."""

from bvh_motion_tools import BvhMotionTools, BvhMotionToolsOptions


def main() -> None:
    # Create with default options
    instance = BvhMotionTools()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = BvhMotionToolsOptions(verbose=True)
    instance = BvhMotionTools(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
