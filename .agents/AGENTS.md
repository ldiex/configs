# Python Usage 
When using bash tool to run a Python script, you should follow this workflow:

1. Declare script dependencies explicitly at the top of the script, or
2. Use `uv add --script` to attach dependencies to the script metadata.

Then run the script with `uv run <script.py>`.

```bash
# Preferred: declare dependencies for the script first
uv add --script example.py 'requests<3' 'rich'

# Then run via uv
uv run example.py
```

For detailed instructions, refer the `uv-package-manager` skill.
