from decman import Module
from decman.plugins import pacman, systemd


class Framework(Module):
    def __init__(self):
        super().__init__(name="hosts-framework")

    @pacman.packages
    def packages(self) -> set[str]:
        return {
            # -----------------------------
            # Intel CPU
            # -----------------------------
            "intel-ucode",
            "intel-lpmd",
            # -----------------------------
            # Intel GPU
            # -----------------------------
            "intel-media-driver",
            "mesa",
            "mesa-utils",
            "vulkan-intel",
            "opencl-mesa",
            "vpl-gpu-rt",
            "lib32-mesa",
            "lib32-opencl-mesa",
            "lib32-vulkan-intel",
        }

    @systemd.units
    def systemd_units(self) -> set[str]:
        return {"intel_lpmd.service"}
