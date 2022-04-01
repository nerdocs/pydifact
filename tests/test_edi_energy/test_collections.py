from edi_energy.energy_collections import (
    EDIEnergyInterchange,
    EDIEnergyMessage,
    EnergySegmentsContainer,
)
from edi_energy.energy_segments import EDISegment
from edi_energy.segmentcollection import AbstractSegmentsContainer
from pydifact.segments import Segment
from pydifact.segmentcollection import Interchange

import conftest

invoice = conftest.data_path_test / "invoice1.edi"
energy_seg_container = EnergySegmentsContainer.from_file(invoice)
energy_seg_mesage = EDIEnergyMessage.from_file(invoice)
energy_seg_interchange = EDIEnergyInterchange.from_file(invoice)


def test_energy_container():

    # verify creation type
    assert isinstance(energy_seg_container, EnergySegmentsContainer)
    # underlying segment type
    assert isinstance(energy_seg_container.segments[0], EDISegment)
    # has qulifier
    assert energy_seg_container.segments[0].qualifier == "UNOA"


def test_energy_message():

    # verify creation type
    assert isinstance(energy_seg_mesage, EDIEnergyMessage)
    # underlying segment type
    assert isinstance(energy_seg_mesage.segments[0], EDISegment)
    # has qulifier
    assert energy_seg_mesage.segments[0].qualifier == "UNOA"


def test_energy_interchange():

    # verify creation type
    print(energy_seg_interchange.segments)
    assert isinstance(energy_seg_interchange, EDIEnergyInterchange)
    assert isinstance(energy_seg_interchange.segments[0], EDISegment)
    # has qulifier
    assert energy_seg_interchange.segments[0].qualifier == "1"
    # underlying segment type
    assert energy_seg_interchange.segments[0]
    assert isinstance(energy_seg_interchange.segments[0], Segment)
    assert isinstance(energy_seg_interchange.segments[2], EDISegment)


def test_interchange_attr():
    assert energy_seg_interchange.sender == "01010000253001"
    assert energy_seg_interchange.control_reference == "PAYO0012101221"
