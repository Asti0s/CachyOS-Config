from decman import Module
from decman.plugins import aur, pacman


class Fonts(Module):
    def __init__(self):
        super().__init__(name="fonts")

    @pacman.packages
    def pacman_packages(self) -> set[str]:
        return {
            "noto-fonts",
            "noto-fonts-emoji",
            "noto-fonts-cjk",
        }

    @aur.packages
    def aur_packages(self) -> set[str]:
        return {
            # Terminal/editor Nerd Font
            "ttf-meslo-nerd-font-powerlevel10k",
        }
