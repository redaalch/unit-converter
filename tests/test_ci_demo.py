"""Temporary failing test for the assignment's CI demonstration."""

import pytest


def test_ci_reports_a_failure():
    pytest.fail("Controlled CI failure: remove this demo after capturing the failed run.")
