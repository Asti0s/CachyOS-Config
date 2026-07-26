import decman

if decman.pacman is None or decman.aur is None or decman.systemd is None:
    raise RuntimeError("decman plugins not initialized")

from modules.base import BaseConfig

decman.modules += [BaseConfig()]

# -----------------------------
# Framework host
# -----------------------------
from hosts.framework import Framework

decman.modules += [Framework()]

# -----------------------------
# Asti0s user
# -----------------------------
from users.asti0s import Asti0s, user_modules

decman.modules += [Asti0s(), *user_modules]
