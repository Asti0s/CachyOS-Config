from decman import Module, Symlink
from decman.plugins import systemd
from helpers import get_sudo_user, user_symlinks


class SSH(Module):
    def __init__(self):
        super().__init__(name="ssh")

    def symlinks(self) -> dict[str, str | Symlink]:
        return user_symlinks(
            {
                ".ssh/config",
            }
        )

    @systemd.user_units
    def systemd_user_units(self) -> dict[str, set[str]]:
        return {
            get_sudo_user(): {
                "ssh-agent.socket",
            }
        }
