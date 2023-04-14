from mapping import SegmentGroup, Segment, Loop
from segmentcollection import Interchange


class DelforTransportInformation(SegmentGroup):
    """SG7 TDT-DTM"""
    transport_details = Segment("TDT", mandatory=True)
    document_date = Segment("DTM", mandatory=False)


class DelforDocumentDetails(SegmentGroup):
    """SG5 DOC-DTM"""
    document_details = Segment("DOC", mandatory=True)
    document_date = Segment("DTM", mandatory=False)


class DelforContactInformation(SegmentGroup):
    """SG3 CTA-COM"""
    contact = Segment("CTA", mandatory=True)
    communication = Segment("COM", mandatory=False)


class DelforSellerBuyerAddressInformation(SegmentGroup):
    """SG2 NAD-LOC-SG3"""
    seller_details = Segment("NAD", mandatory=True)
    location_details = Segment("LOC", mandatory=False)
    buyer_contact_information = Loop(DelforContactInformation, max=1, mandatory=False)


class DelforReferenceDateTimePeriodN(SegmentGroup):
    """SG10,SG1 RFF-DTM"""
    account_reference = Segment("RFF", mandatory=True)
    document_date = Segment("DTM", mandatory=False)


class DelforReferenceDateTimePeriod(SegmentGroup):
    """SG13 RFF-DTM"""
    account_reference = Segment("RFF", mandatory=True)
    document_date = Segment("DTM", mandatory=True)


class DelforSchedulingConditions(SegmentGroup):
    """No segment, but can be looped"""
    scheduling_conditions = Segment("SCC", mandatory=True)


class DelforQtyToBeDelivered(SegmentGroup):
    """SG12 Quantity to be delivered QTY-SCC-DTM-SG13"""
    quantities = Segment("QTY", mandatory=True)
    scheduling_conditions = Loop(DelforSchedulingConditions, max=200, mandatory=True)
    earliest_delivery_date = Segment("DTM", mandatory=True)
    latest_delivery_date = Segment("DTM", mandatory=True)
    referenca_datetime_period = Loop(
        DelforReferenceDateTimePeriod, max=1, mandatory=False)


class DelforQtyCumulativeBackorder(SegmentGroup):
    """SG12 Quantity to be delivered QTY-SCC-DTM-SG13"""
    quantities = Segment("QTY", mandatory=True)
    scheduling_conditions = Loop(DelforSchedulingConditions, max=200, mandatory=False)
    earliest_delivery_date = Segment("DTM", mandatory=False)
    latest_delivery_date = Segment("DTM", mandatory=False)
    referenca_datetime_period = Loop(
        DelforReferenceDateTimePeriod, max=1, mandatory=False)


class DelforQtyDispatch(SegmentGroup):
    """SG12 Quantity to be delivered QTY-SCC-DTM-SG13"""
    quantities = Segment("QTY", mandatory=True)
    scheduling_conditions = Loop(DelforSchedulingConditions, max=200, mandatory=False)
    earliest_delivery_date = Segment("DTM", mandatory=False)
    latest_delivery_date = Segment("DTM", mandatory=False)
    referenca_datetime_period = Loop(
        DelforReferenceDateTimePeriod, max=1, mandatory=True)


class DelforItemInformation(SegmentGroup):
    """SG8 LIN-PIA-IMD-MEA-ALI-GIN-GIR-LOC-DTM-FTX-SG9-SG10-SG11-SG12-SG14"""
    # 9,10,11,12 SG4/SG8
    line_item = Segment("LIN", mandatory=True)
    additional_product_id = Segment("PIA", mandatory=False)
    item_description = Segment("IMD", mandatory=True)
    measure = Segment("MEA", mandatory=False)
    additional_info = Segment("ALI", mandatory=False)
    goods_id_number = Segment("GIN", mandatory=False)
    related_id_number = Segment("GIR", mandatory=False)
    location_identification = Segment("LOC", mandatory=True)
    date_time_period = Segment("DTM", mandatory=True)
    free_text = Segment("FTX", mandatory=False)
    # 13 SG4/SG8/SG10 RFF-DTM
    order_number = Loop(DelforReferenceDateTimePeriodN, max=1, mandatory=True)
    # 14,15,16 SG4/SG8/SG12 QTY-SCC-DTM-SG13 with qty_6063=12 (Dispatch quantity)
    quantity_dispatch = Loop(DelforQtyDispatch, max=1, mandatory=True)
    # 17 SG4/SG8/SG12 QTY-SCC-DTM-SG13 with qty_6063=78 Cumulative quantity scheduled)
    cumulative_quantity_scheduled = Loop(
        DelforQtyCumulativeBackorder, max=1, mandatory=True)
    # 18 SG4/SG8/SG12 QTY-SCC-DTM-SG13 with qty_6063=70 (Cumulative quantity received)
    cumulative_quantity_received = Loop(
        DelforQtyCumulativeBackorder, max=1, mandatory=True)
    # 19 SG4/SG8/SG12 QTY-SCC-DTM-SG13 with qty_6063=83 (Backorder quantity)
    backorder_quantity = Loop(DelforQtyCumulativeBackorder, max=1, mandatory=True)
    # 20,21,22,23 SG4/SG8/SG12 QTY-SCC-DTM-SG13 with qty_6063=113
    qty_to_be_delivered = Loop(DelforQtyToBeDelivered, max=999, mandatory=True)


class DelforDeliveryScheduleDetail(SegmentGroup):
    """SG4 NAD-LOC-FTC-SG5-SG6-SG7-SG8"""
    # 8
    ship_to = Segment("NAD", mandatory=True)
    location_to = Segment("LOC", mandatory=False)
    ftc = Segment("FTC", mandatory=False)
    document_information = Loop(DelforDocumentDetails, max=1, mandatory=False)
    contact_information = Loop(DelforContactInformation, max=1, mandatory=False)
    transport_details = Loop(DelforTransportInformation, max=1, mandatory=False)
    # 9-23
    item_information = Loop(DelforItemInformation, max=1, mandatory=True)


class DelforMessage(SegmentGroup):
    """Groups message due to EDI implementation guide DELFOR UN D96A
    more info https://www.stylusstudio.com/edifact/D96A/DELFOR.htm#SG8 """
    # --- Heading section get checked automatically---

    # interchange_header = Segment("UNB", mandatory=True)
    # 1
    # message_header = Segment("UNH", mandatory=True)
    # 2
    message_id = Segment("BGM", mandatory=True)
    # 3 DTM
    document_date = Segment("DTM", mandatory=True)
    # 4 SG1 RFF-DTM
    schedule_reference = Loop(DelforReferenceDateTimePeriodN, max=1, mandatory=True)
    # 5,6 SG2 NAD-LOC-SG3
    seller_address = Loop(DelforSellerBuyerAddressInformation, max=1, mandatory=True)
    buyer_address = Loop(DelforSellerBuyerAddressInformation, max=1, mandatory=True)
    # 7
    section_splitters = Segment("UNS", mandatory=True)

    # --- Delivery Schedule Detail Section ---
    # 8-23
    delivery_schedule_details = Loop(
        DelforDeliveryScheduleDetail, max=1, mandatory=True)

    # --- Delivery Schedule Summary Section ---
    # 24,24(?)
    uns = Segment("UNS", mandatory=True)
    cnt = Segment("CNT", mandatory=True)


def validate_delfor(inc_message):
    """Validates delfor UND96A message, returns it's object"""
    type_to_parser_dict = {"DELFOR": DelforMessage}
    from_str = Interchange.from_str(inc_message)
    message = next(from_str.Interchange.get_messages())
    cls = type_to_parser_dict.get(message.type)
    if not cls:
        raise NotImplementedError("Unsupported message type '{}'".format(message.type))
    return message
    # obj = cls()
    # obj.from_message(message)


# Occurrences, not a segment groups
class DejitCommunication(SegmentGroup):
    """Not a segment group"""
    communication = Segment("COM", mandatory=False)


class DejitArticleDescription(SegmentGroup):
    """Not a segment group"""
    article_description = Segment("IMD", mandatory=False)


class DejitDatetime(SegmentGroup):
    """Not a segment group"""
    delivery_datetime = Segment("DTM", mandatory=True)


class DejitDatetime(SegmentGroup):
    """Not a segment group"""
    delivery_datetime = Segment("DTM", mandatory=True)


class DejitRelatedIdNumber(SegmentGroup):
    """Not a segment group"""
    related_id_num = Segment("GIR", mandatory=True)


class DejitFreeText(SegmentGroup):
    """Not a segment group"""
    free_text = Segment("FTX", mandatory=True)

class DejitLocation(SegmentGroup):
    """Not a segment group"""
    location = Segment("LOC", mandatory=True)


class DejitManifest(SegmentGroup):
    """Not a segment group"""
    manifest_number = Segment("GIN", mandatory=True)


class DejitAdditionalProductId(SegmentGroup):
    """Not a segment group"""
    additional_product_id = Segment("PIA", mandatory=True)


class DejitAdditionalInformation(SegmentGroup):
    """Not a segment group"""
    additional_info = Segment("ALI", mandatory=True)


class DejitPackage(SegmentGroup):
    """Not a segment group"""
    package = Segment("PAC", mandatory=True)


# Segment groups
class DejitContactInformation(SegmentGroup):
    """SG3,SG11 CTA-COM"""
    contact = Segment("CTA", mandatory=True)
    communication = Loop(DejitCommunication, max=5, mandatory=False)


class DejitNamesAddressFullInformation(SegmentGroup):
    """SG2 NAD-LOC-FTX-SG3  - SG3 Mandatory"""
    details = Segment("NAD", mandatory=True)
    location_details = Loop(DejitLocation, max=10, mandatory=False)
    free_text = Loop(DejitFreeText, max=5, mandatory=False)
    buyer_contact_information = Loop(DejitContactInformation, max=1, mandatory=True)


class DejitNamesAddressInformation(SegmentGroup):
    """SG2 NAD-LOC-FTX-SG3  - SG3 not Mandatory"""
    details = Segment("NAD", mandatory=True)
    location_details = Segment("LOC", mandatory=False)
    free_text = Segment("FTX", mandatory=False)
    contact_information = Loop(DejitContactInformation, max=1, mandatory=False)


class DejitReferenceDateTimePeriodN(SegmentGroup):
    """SG1,SG8,SG13 RFF-DTM"""
    account_reference = Segment("RFF", mandatory=True)
    document_date = Segment("DTM", mandatory=False)


class DejitOrderReference(SegmentGroup):
    """SG8 RFF"""
    reference = Segment("RFF", mandatory=True)


class DejitTransportInformation(SegmentGroup):
    """SG9 TDT-TMD"""
    transport_info = Segment("TDT", mandatory=True)
    transport_movement_details = Segment("TMD", mandatory=False)


class DejitPlaceLocationIdentification(SegmentGroup):
    """SG10 LOC"""
    place_location = Segment("LOC", mandatory=True)
    communication_info = Loop(DejitContactInformation, max=5, mandatory=False)


class DejitPickUpInformation(SegmentGroup):
    """SG12 QTY-SCC-DTM-SG13"""
    pickup_quantity = Segment("QTY", mandatory=True)
    scheduling_conditions = Segment("SCC", mandatory=False)
    pickup_time = Segment("DTM", mandatory=False)
    reference_period = Loop(DejitReferenceDateTimePeriodN, max=99, mandatory=False)


class DejitPriceCurrDate(SegmentGroup):
    """SG14 PRI-CUX-DTM"""
    price = Segment("PRI", mandatory=True)
    currency = Segment("SCC", mandatory=False)
    date_time_period = Loop(DejitDatetime, max=9, mandatory=False)


class DejitLineInformation(SegmentGroup):
    """SG7 LIN-IMD"""
    # 21
    line_item = Segment("LIN", mandatory=True)
    additional_prod_id = Loop(DejitAdditionalProductId, max=10, mandatory=False)
    # 22
    article_descriptions = Loop(DejitArticleDescription, max=99, mandatory=False)
    additional_info = Loop(DejitAdditionalInformation, max=5, mandatory=False)
    related_id_num = Loop(DejitRelatedIdNumber, max=5, mandatory=False)
    free_text = Loop(DejitFreeText, max=5, mandatory=False)
    package = Loop(DejitPackage, max=99, mandatory=False)
    date_period = Loop(DejitDatetime, max=9, mandatory=False)
    # 23 SG8
    order_number = Loop(DejitReferenceDateTimePeriodN, max=9, mandatory=False)
    # 24 SG8
    pus_slb_consignment_no = Loop(DejitReferenceDateTimePeriodN, max=9, mandatory=False)
    transport_info = Loop(DejitTransportInformation, max=9, mandatory=False)
    # 25 SG10
    place_location_id1 = Loop(DejitPlaceLocationIdentification, max=99, mandatory=False)
    # 26 SG10
    place_location_id2 = Loop(DejitPlaceLocationIdentification, max=99, mandatory=False)
    # 27 SG10
    point_of_use = Loop(DejitPlaceLocationIdentification, max=99, mandatory=False)
    # 28,29 SG12
    menge_date = Loop(DejitPickUpInformation, max=999, mandatory=False)
    price_curr_date = Loop(DejitPriceCurrDate, max=9, mandatory=False)


class DejitPackageInformation(SegmentGroup):
    """SG6 PCI-GIN"""
    # 19
    package_info = Segment("PCI", mandatory=True)
    # 20
    manifest_number = Loop(DejitManifest, max=10, mandatory=False)


class DejitItemLines(SegmentGroup):
    """SG5 PAC-SG6"""
    # 18
    package = Segment("PAC", mandatory=True)
    # 19,20 SG6
    package_info = Loop(DejitPackageInformation, max=1, mandatory=False)


class DejitDeliverySequenceDetail(SegmentGroup):
    """SG4 SEQ-SG5-SG7"""
    # 17
    sequence_details = Segment("SEQ", mandatory=True)
    delivery_datetime = Loop(DejitDatetime, max=5, mandatory=False)
    related_id_num = Loop(DejitRelatedIdNumber, max=99, mandatory=False)
    location = Loop(DejitLocation, max=5, mandatory=False)
    # 18,19,20 SG5
    item_lines = Loop(DejitItemLines, max=1, mandatory=True)
    # 21-29 SG7
    line_info = Loop(DejitLineInformation, max=9999, mandatory=False)


class DeljitMessage(SegmentGroup):
    """Groups message due to EDI implementation guide DELJIT UN D.04B S3
    more info https://www.stylusstudio.com/edifact/D04B/DELJIT.htm """

    # --- Heading section gets checked automatically---

    # 1
    # service_str_advice = Segment("UNA", mandatory=False)
    # 2
    # interchange_header = Segment("UNB", mandatory=True)
    # 3
    # message_header = Segment("UNH", mandatory=True)
    # 4
    beginning_msg = Segment("BGM", mandatory=True)
    # 5
    dispatch_call_created = Segment("DTM", mandatory=True)
    # 6
    eta_truck_control = Loop(DejitDatetime, max=10, mandatory=False)
    # 7
    lsp_chattanooga = Loop(DejitDatetime, max=10, mandatory=True)
    free_text = Loop(DejitFreeText, max=5, mandatory=False)
    # 8 SG1
    transport_id = Loop(DejitReferenceDateTimePeriodN, max=10, mandatory=True)
    # 9 SG1
    relation_no = Loop(DejitReferenceDateTimePeriodN, max=10, mandatory=True)
    # 10 SG1
    dispatch_calloff_number = Loop(
        DejitReferenceDateTimePeriodN, max=10, mandatory=True)
    # 11 SG1
    special_transport_number = Loop(
        DejitReferenceDateTimePeriodN, max=10, mandatory=True)
    # 12,13,14 SG2
    driver_information = Loop(
        DejitNamesAddressFullInformation, max=1, mandatory=True)
    # 15 SG2
    supplier_info = Loop(
        DejitNamesAddressInformation, max=1, mandatory=True)
    # 16 SG2
    recipient_info = Loop(
        DejitNamesAddressInformation, max=1, mandatory=True)
    # 17-29 SG4
    delivery_sequence = Loop(
        DejitDeliverySequenceDetail, max=9999, mandatory=True)
    # 30
    message_trailer = Segment("UNT", mandatory=True)
    # 31
    interchange_trailer = Segment("UNZ", mandatory=True)


def validate_deljit(inc_message):
    """Validates deljit D:04B:UND message, returns it's message"""
    type_to_parser_dict = {"DELJIT": DeljitMessage}
    from_str = Interchange.from_str(inc_message)
    message = next(from_str.Interchange.get_messages())
    cls = type_to_parser_dict.get(message.type)
    if not cls:
        raise NotImplementedError("Unsupported message type '{}'".format(message.type))
    return message
