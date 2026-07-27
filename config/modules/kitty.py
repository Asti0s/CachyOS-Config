from decman import Module, Symlink
from decman.plugins import pacman
from helpers import user_symlinks


class Kitty(Module):
    def __init__(self):
        super().__init__(name="kitty")

    @pacman.packages
    def pacman_packages(self) -> set[str]:
        return {
            "kitty",
        }

    def symlinks(self) -> dict[str, str | Symlink]:
        return user_symlinks(
            {
                ".config/kitty/kitty.conf",
                ".config/kitty/current-theme.conf",
            }
        )
