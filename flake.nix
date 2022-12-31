{
  description = "A Flake for godot-docs";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-22.11";
    mach-nix.url = "github:davhau/mach-nix/3.5.0";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };
  outputs = { self, nixpkgs, mach-nix, flake-parts }@inputs:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
        "x86_64-darwin"
      ];
      perSystem = { config, self', inputs', pkgs, system, ... }: {
        packages = let
          mach-nix = (import inputs.mach-nix { pkgs = inputs.mach-nix.inputs.nixpkgs.legacyPackages.${system}; });
          requirements = mach-nix.mkPython {
            requirements = ''
              sphinx==4.4.0
              sphinx_rtd_theme==1.0.0
              sphinx-tabs
              sphinx-notfound-page
              sphinxext-opengraph
              sphinx-tabs
            '';
          };
        in
        {
          default = pkgs.stdenv.mkDerivation {
            name = "godot-docs-html";
            src = self;
            nativeBuildInputs = [
              requirements
              pkgs.python3Packages.setuptools
            ];
            buildPhase = ''
              make html
            '';
            installPhase = ''
              mkdir -p $out
              mv _build/html/* $out
            '';
          };
        };
      };
    };
}
