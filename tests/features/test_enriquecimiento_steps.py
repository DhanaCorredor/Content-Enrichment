"""Pasos (steps) que implementan el escenario Gherkin con pytest-bdd."""

import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("enriquecimiento.feature")


@pytest.mark.skip(reason="pendiente: implementar steps cuando exista el pipeline")
@given("un tema y el idioma destino")
def _():
    raise NotImplementedError
