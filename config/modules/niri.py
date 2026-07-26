from decman import Module, Store
from decman.core.fs import Symlink
from decman.plugins import aur, pacman, systemd
from helpers import get_sudo_user, user_symlinks


class Niri(Module):
    def __init__(self):
        super().__init__(name="niri")

    def on_enable(self, store: Store):
        return

    def symlinks(self) -> dict[str, str | Symlink]:
        return user_symlinks(set())

    @pacman.packages
    def packages(self) -> set[str]:
        return {
            "niri",
            "xwayland-satellite",
            "xdg-desktop-portal-gnome",
            "xdg-desktop-portal-gtk",
            "dms-shell-niri",
            "matugen",
            "cava",
            "qt6-multimedia-ffmpeg",
        }

    @aur.packages
    def aur_packages(self) -> set[str]:
        return {"noctalia-git"}

    @systemd.user_units
    def systemd_user_units(self) -> dict[str, set[str]]:
        return {
            get_sudo_user(): {
                "niri.service",
                "dms.service",
            }
        }
