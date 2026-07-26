import decman
from decman import Module, Store, prg
from helpers import SYSTEM_DIR


class PlymouthTheme(Module):
    def __init__(self):
        super().__init__(name="plymouth_theme")

    def on_enable(self, store: Store):
        prg(["plymouth-set-default-theme", "-R", "circle_hud"])

    def directories(self) -> dict[str, decman.Directory]:
        return {
            "/usr/share/plymouth/themes": decman.Directory(
                source_directory=f"{SYSTEM_DIR}/plymouth-themes"
            )
        }
