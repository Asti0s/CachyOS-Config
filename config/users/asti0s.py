from decman import Module
from decman.plugins import pacman
from modules.kitty import Kitty
from modules.niri import Niri
from modules.plymouth_theme import PlymouthTheme
from modules.ssh import SSH
from modules.vscode import VSCode
from modules.zsh import ZSH


class Asti0s(Module):
    def __init__(self):
        super().__init__(name="users-asti0s")

    @pacman.packages
    def packages(self) -> set[str]:
        return {
            # -----------------------------
            # Shell & env
            # -----------------------------
            "fish",
            "cachyos-fish-config",
            "bash-completion",
            "xdg-user-dirs",
            # -----------------------------
            # Tools
            # -----------------------------
            "nano",
            "nano-syntax-highlighting",
            "git",
            "htop",
            "fastfetch",
            "python",
            "python-packaging",
            "unrar",
            "unzip",
            "which",
            "wget",
            "zen-browser-bin",
            "tree",
            "github-cli",
            "vesktop",
        }


user_modules: list[Module] = [Niri(), VSCode(), PlymouthTheme(), SSH(), ZSH(), Kitty()]
