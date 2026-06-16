"""Pasos (steps) que implementan el escenario Gherkin con pytest-bdd."""

import pytest
from pytest_bdd import scenarios

pytestmark = pytest.mark.skip(reason="pendiente: integracion del pipeline (HU-1..HU-5)")

scenarios("enriquecimiento.feature")
