from decman import Module, Store, prg
from decman.core.fs import Symlink
from decman.plugins import aur
from helpers import get_sudo_user, user_symlinks


class VSCode(Module):
    def __init__(self):
        super().__init__(name="vscode")

    def on_enable(self, store: Store):
        user = get_sudo_user()
        installed = prg(
            ["sudo", "-u", user, "code", "--list-extensions"],
            pty=False,
        )
        installed_set = set(installed.strip().splitlines())

        extensions = [
            "dbaeumer.vscode-eslint",
            "esbenp.prettier-vscode",
            "jeff-hykin.better-cpp-syntax",
            "llvm-vs-code-extensions.vscode-clangd",
            "ms-azuretools.vscode-containers",
            "ms-azuretools.vscode-docker",
            "ms-python.debugpy",
            "ms-python.python",
            "ms-python.vscode-pylance",
            "ms-python.vscode-python-envs",
            "ms-vscode.cmake-tools",
            "ms-vscode.cpp-devtools",
            "ms-vscode.cpptools",
            "ms-vscode.vscode-typescript-next",
            "pkief.material-icon-theme",
            "rust-lang.rust-analyzer",
            "shd101wyy.markdown-preview-enhanced",
            "tamasfe.even-better-toml",
            "twxs.cmake",
            "charliermarsh.ruff",
        ]

        for ext in extensions:
            if ext not in installed_set:
                prg(["sudo", "-u", user, "code", "--install-extension", ext])

    def symlinks(self) -> dict[str, str | Symlink]:
        return user_symlinks({".config/Code/User/settings.json"})

    @aur.packages
    def aur_packages(self) -> set[str]:
        return {"visual-studio-code-bin"}
