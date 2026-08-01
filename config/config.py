import decman
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
