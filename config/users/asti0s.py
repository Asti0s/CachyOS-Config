from decman import Module
from decman.plugins import pacman, systemd
from modules.fastfetch import FastFetch
from modules.kitty import Kitty
from modules.niri import Niri
from modules.plymouth_theme import PlymouthTheme
from modules.ssh import SSH
from modules.sudoers import Sudoers
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
            "xdg-user-dirs",
            # -----------------------------
            # Tools
            # -----------------------------
            "nano",
            "nano-syntax-highlighting",
            "git",
            "htop",
            "python",
            "python-packaging",
            "unrar",
            "unzip",
            "which",
            "wget",
            "tree",
            "github-cli",
            # -----------------------------
            # Apps
            # -----------------------------
            "vesktop",
            "tailscale",
            "zen-browser-bin",
        }

    @systemd.units
    def systemd_units(self) -> set[str]:
        return {
            "tailscaled.service",
        }


user_modules: list[Module] = [
    Niri(),
    VSCode(),
    PlymouthTheme(),
    SSH(),
    ZSH(),
    Kitty(),
    Sudoers(),
    FastFetch(),
]
