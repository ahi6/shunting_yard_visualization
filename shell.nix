{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
   python3
   manim
   ffmpeg
   manim-slides
   uv
   just
   libGL
  ];
  shellHook = ''
      export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath [
      "/run/opengl-driver"
      "/run/opengl-driver-32"
      pkgs.libGL
      ]}:$LD_LIBRARY_PATH"
    '';
}

