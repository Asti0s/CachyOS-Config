from decman import File, Module, Symlink
from decman.plugins import aur, pacman, systemd
from helpers import SYSTEM_DIR


class BaseConfig(Module):
    def __init__(self):
        super().__init__(name="base")

    @pacman.packages
    def packages(self) -> set[str]:
        return {
            # -----------------------------
            # Core system & boot
            # -----------------------------
            "base",
            "base-devel",
            "sudo",
            "os-prober",
            "efibootmgr",
            "systemd-boot-manager",
            "plymouth",
            # -----------------------------
            # CachyOS & maintenance
            # -----------------------------
            "cachyos-settings",
            "cachyos-hooks",
            "cachyos-keyring",
            "cachyos-mirrorlist",
            "cachyos-v3-mirrorlist",
            "cachyos-v4-mirrorlist",
            "cachyos-kernel-manager",
            "chwd",
            "pacman-contrib",
            "rebuild-detector",
            # -----------------------------
            # Linux kernel & firmware
            # -----------------------------
            "linux-cachyos",
            "linux-cachyos-headers",
            "linux-firmware",
            "sof-firmware",
            # -----------------------------
            # Audio stack
            # -----------------------------
            "alsa-firmware",
            "alsa-plugins",
            "alsa-utils",
            "pipewire-alsa",
            "pipewire-pulse",
            "wireplumber",
            "gst-libav",
            "gst-plugin-pipewire",
            "gst-plugin-va",
            "gst-plugins-bad",
            "gst-plugins-ugly",
            # -----------------------------
            # Network
            # -----------------------------
            "networkmanager",
            "openssh",
            "wireless-regdb",
            "ufw",
            "bluez",
            "bluez-hid2hci",
            "bluez-libs",
            "bluez-obex",
            "bluez-utils",
            # -----------------------------
            # File system & storage
            # -----------------------------
            "btrfs-progs",
            "e2fsprogs",
            "dosfstools",
            "cryptsetup",
        }

    @aur.packages
    def packages_aur(self) -> set[str]:
        return {
            "decman",
        }

    @systemd.units
    def systemd_units(self) -> set[str]:
        return {
            "NetworkManager.service",
            "ufw.service",
            "systemd-timesyncd.service",
            "fstrim.timer",
            "bluetooth.service",
        }

    def symlinks(self) -> dict[str, str | Symlink]:
        # Force systemd-resolved as DNS resolver
        return {
            "/etc/resolv.conf": "/run/systemd/resolve/stub-resolv.conf",
        }

    def files(self) -> dict[str, File]:
        return {
            "/etc/mkinitcpio.conf": File(
                source_file=f"{SYSTEM_DIR}/mkinitcpio.conf",
                owner="root",
                group="root",
                permissions=644,
            ),
            # Tell NetworkManager to use systemd-resolved for DNS resolution
            "/etc/NetworkManager/conf.d/dns.conf": File(
                source_file=SYSTEM_DIR + "/NetworkManager/dns.conf",
                group="root",
                owner="root",
                permissions=644,
            ),
        }
