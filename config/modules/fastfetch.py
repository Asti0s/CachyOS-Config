from decman import Module, Symlink
from decman.plugins import pacman
from helpers import user_symlinks


class FastFetch(Module):
    def __init__(self):
        super().__init__(name="fastfetch")

    @pacman.packages
    def packages(self) -> set[str]:
        return {
            "fastfetch",
        }

    def symlinks(self) -> dict[str, str | Symlink]:
        return user_symlinks(
            {
                ".config/fastfetch/config.jsonc",
                ".config/fastfetch/battery",
            }
        )
