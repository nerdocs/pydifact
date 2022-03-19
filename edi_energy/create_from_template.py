import warnings
from pathlib import Path
from typing import Dict, Union

from ..utils.files import ensure_path, load_json, save_as_json

Warning("switching Import from ea.EdiTxMessage to ea.edifact.EdiTxTMessage")

TSIMSGS = r"C:\Users\ZX6255\repositories\Operative_Work\B2B_Testing\Test_Packages\Vorlieferant\TSIMSG"

template_name = "UTILMD__9800505300009_9800383000003_20211202_THE112878303.txt"
_template_balancing_group = "THE0BFH020530000"
_template_ref_id = "THE112878303"

MESSAGE_TEMPLATE = Path(TSIMSGS) / template_name

# deactivate to 2022
MESSAGES_TO_CREATE = {
    "Implemenation_test": "GASPOOLEH5190000",
    # "OMV_clearing_2": "GASPOOLEL2790000",
    # "VNG_clearing_1": "NCLB400124570000",
    # "VNG_clearing_2": "NCHB400116320000",
    # "OMV_old_1": "THE0BFH020530000",
    # "OMV_old_2": "THE0BFL020540000",
    # "VNG_old_1": "THE0BFL006440000",
    # "VNG_old_2": "THE0BFH002040000",
}


def main() -> None:
    """test doc"""
    template = EdiTxTMessage.load_file(TSIMSGS, template_name)
    template.set_balancing_group(_template_balancing_group)
    template.set_ref_id(_template_ref_id)

    created_messages = MessageFactory.create_from_template(template, MESSAGES_TO_CREATE)
    MessageFactory.export_messages(TSIMSGS, created_messages)


class EdiTxTMessage:
    def __init__(self) -> None:
        self.ref_id = ""
        self.balancing_group = ""
        self.date = ""
        self.system = ""
        self.rff = ""

    @classmethod
    def load_file(cls, file_dir: Union[str, Path], file_name: Union[str, Path] = None):
        message = EdiTxTMessage()

        if file_name:
            message.dir_ = ensure_path(file_dir)
            message.name = ensure_path(file_name)
        else:
            full_file_path = ensure_path(file_dir)
            message.dir_ = full_file_path.parent
            message.name = full_file_path.name

        with open(str(message.path)) as file:
            content = file.read()

        message.content = content
        return message

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str) -> None:
        self._content = content

    @property
    def path(self):
        return self.dir_ / self.name

    def set_ref_id(self, val, update: bool = False):
        if self.ref_id and self.ref_id == val:
            return  # skip is value to set is equal
        if update:
            self.update_content(self.ref_id, val)
        self.ref_id = val

    def set_balancing_group(self, val, update: bool = False):
        if self.balancing_group and self.balancing_group == val:
            return  # skip is value to set is equal
        if update:
            self.update_content(self.balancing_group, val)
        self.balancing_group = val

    def set_date(self, val, update: bool = False):
        if self.date and self.date == val:
            return  # skip is value to set is equal
        if update:
            self.update_content(self.date, val)
        self.date = val

    def set_system(self, val, update: bool = False):
        if self.system and self.system == val:
            return  # skip is value to set is equal
        if update:
            self.update_content(self.system, val)
        self.system = val

    def set_rff(self, val, update: bool = False):
        if self.rff and self.rff == val:
            return  # skip is value to set is equal
        if update:
            self.update_content(":" + self.rff + "'", ":" + val + "'")
        self.rff = val

    def update_content(self, old: str, new_: str, max_occurences: int = None) -> None:
        if max_occurences:
            self.content = self.content.replace(old, new_, max_occurences)
        else:
            self.content = self.content.replace(old, new_)


class MessageFactory:
    @classmethod
    def create_new_message(cls, template: EdiTxTMessage) -> EdiTxTMessage:
        message = EdiTxTMessage()
        for key, val in vars(template).items():
            setattr(message, key, val)
        return message

    @classmethod
    def modify_content(
        cls, message: EdiTxTMessage, balancing_group: str, ref_id
    ) -> str:
        message.set_balancing_group(balancing_group, True)
        message.set_ref_id(ref_id, True)
        return message

    @classmethod
    def change_system(cls, message: EdiTxTMessage, system: str):
        id = get_test_id()
        message.set_ref_id(id, True)
        message.set_system(system, True)

    @classmethod
    def change_rff(cls, message: EdiTxTMessage, rff: str):
        id = get_test_id()
        message.set_ref_id(id, True)
        message.set_rff(rff, True)

    @classmethod
    def create_from_template(
        cls,
        template: EdiTxTMessage,
        files_to_create: Dict,
    ) -> Dict[str, EdiTxTMessage]:
        messages = []

        for bg in files_to_create.values():
            id = get_test_id()
            new_ = MessageFactory.create_new_message(template)
            # new_ = MessageFactory.modify_content(new_, bg, id)
            new_.set_ref_id(id, True)
            messages.append(new_)

        return dict(zip(files_to_create.keys(), messages))

    def append_to_message_name(created_messages: Dict[str, EdiTxTMessage], str_: str):
        # combine message name and month
        return {
            "-".join((name, str_)): message
            for name, message in created_messages.items()
        }

    @classmethod
    def change_date(cls, created_messages: Dict[str, EdiTxTMessage], date: str):
        for _, message in created_messages.items():
            message.set_date(date, True)

    @classmethod
    def export_messages(
        cls,
        export_dir: Union[str, Path],
        created_messages: Dict[str, EdiTxTMessage],
        template_ref_id: str,
        append_destination: bool = True,
    ) -> None:
        for test_name, message in created_messages.items():
            export_name = ensure_path(
                message.path.name.replace(template_ref_id, message.ref_id)
            )

            # combine file name, test name and ref id
            file_name = (
                export_name.with_stem("_".join((export_name.stem, test_name)))
                if append_destination
                else export_name.name
            )

            full_file_name = ensure_path(export_dir) / file_name

            with open(full_file_name, "w") as new_f:
                new_f.write(message.content)

    @classmethod
    def export_new_system(
        cls,
        export_dir,
        created_message: EdiTxTMessage,
        template_ref_id,
        template_system,
    ):

        export_name = ensure_path(
            created_message.path.name.replace(template_ref_id, created_message.ref_id)
        )

        export_name = export_name.name.replace(template_system, created_message.system)

        # combine file name, test name and ref id
        file_name = ensure_path(export_dir) / export_name

        with open(file_name, "w") as new_f:
            new_f.write(created_message.content)

        print(f"exported\t{file_name.name}")

    @classmethod
    def export_new_rff(
        cls, export_dir, created_message: EdiTxTMessage, template_ref_id, template_rff
    ):

        export_name = ensure_path(
            created_message.path.name.replace(template_ref_id, created_message.ref_id)
        )

        export_name = export_name.name.replace(template_rff, created_message.rff)

        # combine file name, test name and ref id
        file_name = ensure_path(export_dir) / export_name

        with open(file_name, "w") as new_f:
            new_f.write(created_message.content)
        print(f"exported\t{file_name.name}")

    @classmethod
    def export_message(cls, export_dir: Path, created_message: EdiTxTMessage):
        """writes edi txt message obj to file

        Args:
            export_dir (Path): _description_
            created_message (EdiTxTMessage): _description_
        """

        export_name = ensure_path(created_message.path.name)

        # combine file name, test name and ref id
        file_name = ensure_path(export_dir) / export_name

        with open(file_name, "w") as new_f:
            new_f.write(created_message.content)
        print(f"exported\t{file_name.name}")


def get_test_id(count: bool = True) -> str:
    """enables a running message ref id"""
    path_config = Path(__file__).parent / "config.json"
    key_id = "current_test_id"

    current_id = load_json(path_config)[key_id]

    if not count:
        warnings.warn("Using same Ref ID for this test. May override File.")
    else:
        current_id += 1

    save_as_json({key_id: current_id}, path_config)

    return "TEST" + "{:08d}".format(current_id)
