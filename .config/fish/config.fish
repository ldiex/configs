if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting ""
set -g fish_key_bindings fish_vi_key_bindings

alias ls 'eza --icons'
alias cat 'bat'
alias fopen 'fzf | xargs open'

# fish_config command to open config in Neovim
function fish_config
    nvim ~/.config/fish/config.fish
end


# uv
fish_add_path "/Users/tianlinpan/.local/bin"
