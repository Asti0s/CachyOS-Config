<div align="center">

# CachyOS Config

[![Distribution](https://img.shields.io/badge/OS-CachyOS-008080?style=for-the-badge&logo=arch-linux&logoColor=white)](https://cachyos.org/) [![Compositor](https://img.shields.io/badge/Compositor-Niri-darkblue?style=for-the-badge)](https://github.com/YaLTeR/niri)
[![Config](https://img.shields.io/badge/Manager-decman-orange?style=for-the-badge)](https://github.com/kiviktnm/decman) [![Language](https://img.shields.io/badge/Language-Python_3-yellow?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

A ***mostly* reproducible** and **declarative** system configuration, managed via [decman](https://github.com/kiviktnm/decman).

</div>

---

> [!WARNING]
> **WIP / Active Rice**
> This setup is actively being riced and configured. Screenshots and showcases will be added once the visual side settles down!

Everything (packages, dotfiles, systemd units, and user setup) is declared as code, so you can rebuild the exact same environment from scratch on any machine.

---

## 🛠️ Core Stack

| Layer | Tool | Description |
| :--- | :--- | :--- |
| **Distribution** | [CachyOS](https://cachyos.org/) | Arch-based distro optimized for performance |
| **Config Manager**| [decman](https://github.com/kiviktnm/decman) | Declarative package & dotfile manager |
| **Display Server**| [Wayland](https://wayland.freedesktop.org/) | Next-generation display server protocol |
| **Compositor** | [Niri](https://github.com/YaLTeR/niri) | Scrollable-tiling Wayland compositor |
| **Desktop Shell** | [DMS](https://github.com/AvengeMedia/DankMaterialShell) | *(Testing / Not final)* Material shell |
| **Terminal** | [Kitty](https://sw.kovidgoyal.net/kitty/) | GPU-accelerated terminal emulator |
| **Shell** | [Zsh](https://www.zsh.org/) | Managed with [Antidote](https://getantidote.github.io/) |

---

## ✨ Features

* 📦 **Declarative package management** — All packages are declared per-module and installed through `pacman` (with AUR support).
* 🔗 **Reproducible dotfiles** — Configuration files are symlinked from the repo into place, keeping everything versioned in Git.
* 🧩 **Modular structure** — Each component (shell, editor, compositor, SSH, etc.) lives in its own dedicated module.
* ⚙️ **Systemd integration** — User services and sockets are declared and enabled declaratively.

---

## 📂 Project Structure

```text
config/
├── config.py          # Entry point
├── helpers.py         # Shared helpers
├── hosts/             # Hardware-specific configuration (per machine)
├── modules/           # Per-component modules (zsh, niri, ssh, ...)
└── users/             # Which modules each user wants
dotfiles/              # Dotfiles symlinked into the system
system/                # System-level config (mkinitcpio, sudoers, ...)

```

* **`hosts/`** — Hardware-specific configuration. This is where machine-specific differences live (GPU, CPU, drivers, machine-specific services, etc.), so the same repo can be reused across different machines.
* **`users/`** — Per-user configuration. This defines *which modules* each user wants enabled, so different users on the same machine can have different setups.

---

## 🚀 Usage

### 1. Install decman

`decman` is available on the AUR. It is recommended to install it manually without an AUR helper, as `decman` manages the AUR itself:

```bash
git clone [https://aur.archlinux.org/decman.git](https://aur.archlinux.org/decman.git)
cd decman
makepkg -si
```

### 2. Clone this repo

```bash
git clone [https://github.com/Asti0s/CachyOS-Config](https://github.com/Asti0s/CachyOS-Config)
cd CachyOS-Config
```

### 3. Apply the configuration

```bash
sudo decman --source ./config/config.py
```

---

## 📦 Modules

* **zsh** — Shell setup (Antidote, Powerlevel10k, fzf-tab, autosuggestions)
* **niri** — Wayland compositor + portals + keyring
* **ssh** — SSH agent & config
* **kitty** — Terminal emulator
* **fastfetch** — System information display
* **vscode** — Editor configuration
* *...and more!*

---

## 🤔 Why not NixOS?

NixOS pioneered declarative system management, so why not just use it? As [the creator of decman](https://github.com/kiviktnm/decman#why-not-use-nixos) puts it:

> [!NOTE]
> *"I tried NixOS in the past, but it had some issues that caused me to create decman for Arch Linux instead. In my opinion:*
> * *NixOS forces you to do everything the Nix way.*
> * *NixOS requires learning a new domain specific language.*
> * *NixOS is extreme when it comes to declaration. Sometimes you don't want everything to be managed declaratively."*
>
>

I fully share this view. For my desktop setup, this trade-off makes much more sense:

* **No abstraction layer** — Instead of learning the Nix language, everything is declared in standard Python, which can directly run Bash when needed. Dotfiles remain in their native formats (pure KDL, JSON, Zsh) rather than being wrapped in Nix syntax.
* **Bidirectional dotfiles** — Nix symlinks point to a read-only store. Here, they point directly to this repo. If I tweak a setting in VS Code's UI, it writes straight to my local git repo—I just commit and push.
* **Pragmatic flexibility** — I get declarative packages, dotfiles, and systemd units while keeping standard Arch/CachyOS flexibility when needed.

I'm aware this means giving up Nix's atomicity and bit-for-bit reproducibility, but trading that for simplicity and workflow comfort is completely worth it for me.
