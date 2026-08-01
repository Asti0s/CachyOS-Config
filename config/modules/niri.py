from decman import Module, Store, Symlink
from decman.plugins import aur, pacman, systemd
from helpers import get_sudo_user, user_symlinks


class Niri(Module):
    def __init__(self):
        super().__init__(name="niri")

    def on_enable(self, store: Store):
        return

    def symlinks(self) -> dict[str, str | Symlink]:
        return user_symlinks(
            {
                ".config/xdg-desktop-portal/niri-portals.conf",
                ".config/niri/config.kdl",
                ".config/niri/input.kdl",
                ".config/niri/monitors.kdl",
                ".config/niri/keybindings.kdl",
                ".config/niri/layout.kdl",
                ".config/niri/window-rules.kdl",
                ".config/flavours/schemes/Catppuccin Mocha/Catppuccin Mocha.yaml",
                ".config/flavours/schemes/Catppuccin Latte/Catppuccin Latte.yaml",
                ".config/flavours/config.toml",
            }
        )

    @pacman.packages
    def packages(self) -> set[str]:
        return {
            "niri",
            "xwayland-satellite",
            # Portals
            "xdg-desktop-portal",
            "xdg-desktop-portal-gnome",
            "xdg-desktop-portal-gtk",
            "gnome-keyring",
            # DMS
            "dms-shell-niri",
            "cava",
            "qt6-multimedia-ffmpeg",
            "matugen",
            # Utils
            "playerctl",
            "brightnessctl",
        }

    @aur.packages
    def aur_packages(self) -> set[str]:
        return {
            "noctalia-git",
            "flavours",
        }

    @systemd.user_units
    def systemd_user_units(self) -> dict[str, set[str]]:
        return {
            get_sudo_user(): {
                "niri.service",
                "dms.service",
            }
        }
