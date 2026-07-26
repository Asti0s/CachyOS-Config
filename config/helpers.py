import os

from decman.core.fs import Symlink

# __file__ = config/_helpers.py → parent = config/ → grandparent = repo root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTFILES_DIR = f"{REPO_ROOT}/dotfiles"
SYSTEM_DIR = f"{REPO_ROOT}/system"


def get_sudo_user() -> str:
    user = os.environ.get("SUDO_USER")
    if user is None:
        raise RuntimeError("SUDO_USER is not set — run decman with sudo")
    return user


def user_symlinks(dotfiles: set[str]) -> dict[str, str | Symlink]:
    user = get_sudo_user()
    user_config = f"/home/{user}"
    return {
        f"{user_config}/{df}": Symlink(f"{DOTFILES_DIR}/{df}", owner=user, group=user)
        for df in dotfiles
    }
