# bvh_motion_tools

Load, retarget, and blend BVH motions with a clean Python API.

## Installation

```bash
pip install bvh_motion_tools
```

## Quick Start

```python
from bvh_motion_tools import BvhMotionTools

instance = BvhMotionTools()
result = instance.run()
print(result)
```

## Features

- BVH parser to skeleton + per-joint transforms
- Retargeting between skeletons with joint mapping
- Motion trimming, looping, and time-warp resampling
- Blend and concatenate clips with root-motion options

## API Reference

### `BvhMotionTools`

#### Constructor

```python
BvhMotionTools(options: BvhMotionToolsOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `BvhMotionToolsResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/bvh_motion_tools/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
