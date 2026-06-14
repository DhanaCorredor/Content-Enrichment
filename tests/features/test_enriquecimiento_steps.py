"""Pasos (steps) que implementan el escenario Gherkin con pytest-bdd."""

import pytest
from pytest_bdd import scenarios

# El escenario prueba el flujo completo, que necesita la clase Pipeline (aun no
# implementada). Hasta la fase de integracion (HU-1..HU-5) marcamos el escenario
# como pendiente para no romper la suite.
pytestmark = pytest.mark.skip(reason="pendiente: integracion del pipeline (HU-1..HU-5)")

scenarios("enriquecimiento.feature")
