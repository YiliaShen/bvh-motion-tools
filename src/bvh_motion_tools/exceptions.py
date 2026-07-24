"""Custom exceptions for bvh_motion_tools."""

from __future__ import annotations


class BvhMotionToolsError(Exception):
    """Base exception for all BvhMotionTools errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(BvhMotionToolsError):
    """Raised when the SDK is misconfigured."""


class ValidationError(BvhMotionToolsError):
    """Raised when input validation fails."""


class TimeoutError(BvhMotionToolsError):
    """Raised when an operation exceeds its time limit."""
