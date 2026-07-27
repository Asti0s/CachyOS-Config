from decman import Module, Store, Symlink, prg
from decman.plugins import aur, pacman
from helpers import get_sudo_user, user_symlinks


class ZSH(Module):
    def __init__(self):
        super().__init__(name="zsh")

    def on_enable(self, store: Store):
        user = get_sudo_user()
        prg(["sudo", "-u", user, "chsh", "-s", "/usr/bin/zsh"])

    @pacman.packages
    def pacman_packages(self) -> set[str]:
        return {"zsh"}

    @aur.packages
    def aur_packages(self) -> set[str]:
        return {
            "zsh-antidote",
            "ttf-meslo-nerd-font-powerlevel10k",
        }

    def symlinks(self) -> dict[str, str | Symlink]:
        return user_symlinks(
            {
                ".zsh_plugins.txt",
                ".zshrc",
                ".p10k.zsh",
            }
        )
