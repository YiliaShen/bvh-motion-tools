"""Type definitions for bvh_motion_tools."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class BvhMotionToolsOptions:
    """Configuration options for BvhMotionTools.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: BVH parser to skeleton + per-joint transforms
        feature_2: Configuration for: Retargeting between skeletons with joint mapping
        feature_3: Configuration for: Motion trimming, looping, and time-warp resampling
        feature_4: Configuration for: Blend and concatenate clips with root-motion options
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None
    feature_4: Optional[dict[str, Any]] = None


@dataclass
class BvhMotionToolsResult:
    """Result returned by BvhMotionTools operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
