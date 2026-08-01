from decman import File, Module
from helpers import SYSTEM_DIR


class Sudoers(Module):
    def __init__(self):
        super().__init__(name="sudoers")

    def files(self) -> dict[str, File]:
        return {
            "/etc/sudoers.d/custom": File(
                source_file=SYSTEM_DIR + "/sudoers.d/custom",
                group="root",
                owner="root",
                permissions=440,
            )
        }
