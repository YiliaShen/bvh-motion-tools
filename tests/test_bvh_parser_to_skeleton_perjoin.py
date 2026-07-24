"""Tests for bvh_motion_tools."""

from bvh_motion_tools import BvhMotionTools, BvhMotionToolsOptions


class TestBvhMotionTools:
    def test_create_instance_with_defaults(self) -> None:
        instance = BvhMotionTools()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = BvhMotionToolsOptions(verbose=True)
        instance = BvhMotionTools(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = BvhMotionTools()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = BvhMotionTools()
        result = instance.run()
        assert result.error is None
