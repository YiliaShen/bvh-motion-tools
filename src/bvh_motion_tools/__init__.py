"""
bvh_motion_tools - Load, retarget, and blend BVH motions with a clean Python API.
"""

__version__ = "0.1.0"

from .bvh_parser_to_skeleton_perjoin import BvhMotionTools
from .types import BvhMotionToolsOptions, BvhMotionToolsResult
from .exceptions import BvhMotionToolsError, ConfigurationError, ValidationError

__all__ = [
    "BvhMotionTools",
    "BvhMotionToolsOptions",
    "BvhMotionToolsResult",
    "BvhMotionToolsError",
    "ConfigurationError",
    "ValidationError",
]
