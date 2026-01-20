#!/bin/bash

echo "Setting up config files..."

# Create ~/.config if it doesn't exist
mkdir -p ~/.config

cp -r fish ~/.config/fish
cp -r ghostty ~/.config/ghostty

# Copy .claude directory
cp -r .claude ~/

echo "Config files set up successfully!"

echo "Installing packages using Homebrew..."

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "Error: Homebrew is not installed. Please install Homebrew first."
    echo "Visit https://brew.sh for installation instructions."
    exit 1
fi

# Install packages
packages=(
    "fzf"       # Fuzzy finder
    "fish"      # Fish shell
    "fd"        # Fast file finder
    "bat"       # Cat clone with syntax highlighting
    "lazygit"   # Terminal UI for git
    "uv"        # Python package installer
    "eza"       # Modern ls replacement
    "neovim"    # Modern Vim editor
    "btop"      # Resource monitor
    "aria2"     # Download utility
    "ghossty"   # Terminal
)

for package in "${packages[@]}"; do
    echo "Installing $package..."
    brew install "$package"
done

echo "All packages installed successfully!"
