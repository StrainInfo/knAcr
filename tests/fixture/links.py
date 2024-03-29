import pytest

from knacr.container.acr_db import CatArgs


@pytest.fixture()
def ccno_dsmz_1() -> tuple[int, CatArgs]:
    return 1, CatArgs(acr="DSM", id="1", pre="", suf="", core="1")


@pytest.fixture()
def ccno_iam_1() -> tuple[int, CatArgs]:
    return 15, CatArgs(acr="IAM", id="1", pre="", suf="", core="1")


@pytest.fixture()
def ccno_nrrl_1() -> tuple[int, CatArgs]:
    return 17, CatArgs(acr="NRRL", id="B-1", pre="B", suf="", core="1")


@pytest.fixture()
def ccno_dcg_1() -> tuple[int, CatArgs]:
    return 82, CatArgs(acr="DCG", id="1", pre="", suf="", core="1")


@pytest.fixture()
def ccno_lmg_1_1() -> tuple[int, CatArgs]:
    return 2, CatArgs(acr="LMG", id="1.1", pre="", suf="", core="1.1")
