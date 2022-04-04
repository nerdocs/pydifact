import conftest
import pytest

from pydifact.edi_analyzer.analyze import Index, compare_segments_to_index
from pydifact.edi_energy.energy_formats import EDIenergy
from pydifact.edi_energy.energy_segments import RFF, EDISegment

file_path = (
    conftest.data_path
    / "MSCONS_TL_9906311000005_9904771000003_20220315_100698625960.txt"
)
mscons = EDIenergy.from_file(file_path)


smpl_lgth = 20

idx_list = list(range(smpl_lgth))
idx_dict = dict(zip(range(smpl_lgth), range(smpl_lgth)))


@pytest.mark.parametrize("idx_src", [idx_list, idx_dict])
def test_Index_creation(idx_src):
    assert isinstance(Index(idx_src), Index)


def test_creation_from_list():
    assert Index(idx_list).check(str(smpl_lgth // 2))
    assert not Index(idx_list).check(str(smpl_lgth + 1))


def test_creation_from_dict():
    assert Index(idx_dict).check(str(smpl_lgth // 2)) == (True, str(smpl_lgth // 2))
    assert Index(idx_dict).check_dict(str(smpl_lgth // 2)) == (
        True,
        str(smpl_lgth // 2),
    )
    # test wrapper
    assert Index(idx_dict).check_dict(str(smpl_lgth // 2)) == Index(idx_dict).check(
        str(smpl_lgth // 2)
    )
    assert not Index(idx_dict).check(str(smpl_lgth + 1))


def test_index_various_input_types():
    idx_list.append("5020436373085")
    index = Index(idx_list)

    assert set(type(i) for i in index.index) == set([str])  # all alements are strings
    assert "5020436373085" == index.index[-1]
    assert index.check("5020436373085")
    assert not index.check("502043637308XX")


def test_index_with_message():
    assert (
        compare_segments_to_index(mscons, RFF, idx_list, RFF.is_Z13)
        == "ID-Code: 13025\t count: 1\t whitelisted: False\n"
    )
    idx_list.append("13025")
    assert (
        compare_segments_to_index(mscons, RFF, idx_list, RFF.is_Z13)
        == "ID-Code: 13025\t count: 1\t whitelisted: True\n"
    )
