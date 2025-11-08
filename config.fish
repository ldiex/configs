if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting ""

alias ls 'eza --icons'
alias cat 'bat'

# fish_config command to open config in Neovim
function fish_config
    nvim ~/.config/fish/config.fish
end


