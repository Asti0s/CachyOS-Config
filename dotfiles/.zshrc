# -------------------------------------------------------------------
# Powerlevel10k Configuration
# -------------------------------------------------------------------

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi



# -------------------------------------------------------------------
# Antidote Plugin Manager Initialization
# -------------------------------------------------------------------

# Define paths for antidote's static plugins files
zsh_plugins=${ZDOTDIR:-$HOME}/.zsh_plugins

# Ensure the required plugin source file exists
if [[ ! -f ${zsh_plugins}.txt ]]; then
  print -P "%F{red}Error: Required plugin file '${zsh_plugins}.txt' does not exist!%f" >&2
  return 1
fi

# Automatically rebuild the static plugin file in a subshell if .txt is newer than .zsh
if [[ ! ${zsh_plugins}.zsh -nt ${zsh_plugins}.txt ]]; then
  if [[ -r /usr/share/zsh-antidote/antidote.zsh ]]; then
    (
      source /usr/share/zsh-antidote/antidote.zsh
      antidote bundle <${zsh_plugins}.txt >|${zsh_plugins}.zsh
    )
  else
    print -P "%F{red}Error: antidote is not found at /usr/share/zsh-antidote/antidote.zsh%f" >&2
    return 1
  fi
fi

# Load the static plugins file
source ${zsh_plugins}.zsh



# -------------------------------------------------------------------
# Performance & Completion Settings
# -------------------------------------------------------------------

# Speed up completion by skipping insecure directory checks
export ZSH_DISABLE_COMPFIX="true"

# Initialize completion engine with daily caching and binary compilation
autoload -Uz compinit

# Ensure extended globbing is enabled so (#q...) is parsed correctly
setopt LOCAL_OPTIONS EXTENDED_GLOB

# Check if .zcompdump is older than 24 hours or missing (m1)
for dump in ~/.zcompdump(#qN.m1); do
  compinit
  # Automatically compile the dump file into a binary format for speed
  [[ -f ~/.zcompdump ]] && zcompile -R ~/.zcompdump.zwc ~/.zcompdump
done

# If a fresh dump exists, load it strictly from cache (-C) using the compiled version if available
if [[ -z ${dump:-} ]]; then
  if [[ -s ~/.zcompdump.zwc ]]; then
    compinit -C -d ~/.zcompdump
  else
    compinit -C
  fi
fi

# Non-Case Sensitive Completion
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'



# -------------------------------------------------------------------
# Shell Options & History Configuration
# -------------------------------------------------------------------

HISTFILE="${ZDOTDIR:-$HOME}/.zsh_history"
HISTSIZE=10000
SAVEHIST=10000

setopt EXTENDED_HISTORY       # Write the timestamp and duration to history
setopt SHARE_HISTORY          # Share history across all sessions
setopt HIST_EXPIRE_DUPS_FIRST # Expire duplicate events first
setopt HIST_IGNORE_DUPS       # Do not record an event that was just recorded
setopt HIST_IGNORE_ALL_DUPS   # Delete an old recorded event if a new duplicate is added
setopt HIST_FIND_NO_DUPS      # Do not display a previously found event
setopt AUTO_CD                # If a command isn't a valid command, try to cd into it


# -------------------------------------------------------------------
# Key Bindings (History Substring Search & Navigation)
# -------------------------------------------------------------------

# Bind Up/Down arrows for history substring search
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down

# Bind Ctrl + Left/Right arrows to jump across words
bindkey '^[[1;5D' backward-word
bindkey '^[[1;5C' forward-word



# -------------------------------------------------------------------
# Theme Configuration (Powerlevel10k - Skipped in TTY)
# -------------------------------------------------------------------

if [[ "$TERM" != "linux" ]]; then
  # Source p10k theme
  [[ ! -f ${ZDOTDIR:-$HOME}/.cache/antidote/github.com/romkatv/powerlevel10k/powerlevel10k.zsh-theme ]] \
    || source ${ZDOTDIR:-$HOME}/.cache/antidote/github.com/romkatv/powerlevel10k/powerlevel10k.zsh-theme

  # Load p10k configuration if it exists
  [[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
else
  # Fallback plain prompt for standard TTY where Nerd Fonts won't work
  PROMPT='%n@%m %~ %# '
fi

# Specify Kitty terminal emulator
export TERM="xterm-kitty"
