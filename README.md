# Shunting yard algorithm visualization
This is a script for an animation to visualize how the Shunting yard algorithm works, as well as how the resulting reverse Polish notation (RPN) is computed.

I had no regard for the maintainability of this script, as I do not intend to return to it. It may be unreadable/unoptimized.

Note: The labels are in Czech.

## Video


https://github.com/user-attachments/assets/d9146414-63bd-419d-a403-60922ebc51c7



## How to run locally
Dependencies are managed using the Nix package manager and defined in `shell.nix`. Using direnv is recommended.

Useful manim and manim-slides commands are saved in the `justfile`.

### Example usage
Run locally:
```just run```

Render to video:
```just render```

Export to self-contained HTML:
```just render html```

Export to PowerPoint:
```just render pptx```
