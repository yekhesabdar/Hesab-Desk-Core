# RustDesk Project Context

This directory contains the source code for RustDesk, a full-featured open-source remote desktop solution written in Rust. It supports multiple platforms including Windows, Linux, macOS, Android, and iOS.

## Project Overview

- **Main Technologies**: Rust, Flutter (Modern UI), Sciter (Legacy UI), vcpkg (dependency management).
- **Architecture**:
  - **`libs/hbb_common`**: Core common logic, including video codecs, configuration, networking (TCP/UDP), protobuf definitions, and file transfer utilities.
  - **`libs/scrap`**: Screen capture library with support for various platforms (including Wayland on Linux).
  - **`libs/enigo`**: Platform-specific keyboard and mouse control.
  - **`libs/clipboard`**: Cross-platform clipboard implementation.
  - **`src/server`**: Audio, clipboard, input, and video services.
  - **`src/client.rs`**: Peer-to-peer connection logic.
  - **`flutter/`**: Modern UI implementation using Flutter for desktop and mobile.
  - **`src/ui/`**: Legacy Sciter-based UI (deprecated).

## Building and Running

### Prerequisites
- **Rust**: Latest stable version (specified as 1.75 in `Cargo.toml`).
- **vcpkg**: Required for C++ dependencies (`libvpx`, `libyuv`, `opus`, `aom`). Set `VCPKG_ROOT` environment variable.
- **Sciter**: If running the legacy UI version, the Sciter dynamic library is required in the library path.

### Key Commands
- **Run Desktop (Rust)**: `cargo run` (Builds and runs the desktop application, requires libsciter).
- **Build Flutter (Desktop)**: `python3 build.py --flutter`
- **Build Flutter Release**: `python3 build.py --flutter --release`
- **Build with Hardware Codec**: `python3 build.py --hwcodec`
- **Run Flutter (Development)**: `cd flutter && flutter run`
- **Build Mobile**: `cd flutter && flutter build android` or `cd flutter && flutter build ios`
- **Docker Build**:
  - Build image: `docker build -t "rustdesk-builder" .`
  - Run build: `docker run --rm -it -v $PWD:/home/user/rustdesk rustdesk-builder`

### Testing
- **Rust Tests**: `cargo test`
- **Flutter Tests**: `cd flutter && flutter test`

## Development Conventions

- **Code Style**: Standard Rust idioms and formatting. Use `cargo fmt` and `cargo clippy`.
- **Feature Flags**:
  - `hwcodec`: Enable hardware video encoding/decoding.
  - `flutter`: Enable Flutter-based UI.
  - `vram`: VRAM optimization (Windows only).
  - `unix-file-copy-paste`: Enable Unix file clipboard support.
- **Configuration**: Main configuration logic is located in `libs/hbb_common/src/config.rs`. It manages settings, local configs, and display options.
- **Cross-Platform**: Be mindful of platform-specific code in `src/platform/` and use `cfg` attributes appropriately.
- **Build Scripts**: `build.py` is the primary entry point for complex builds and packaging.

## Key Files
- `Cargo.toml`: Workspace configuration and dependencies.
- `build.py`: Main build and packaging script.
- `CLAUDE.md`: Comprehensive development guide and architecture summary.
- `src/main.rs`: Entry point for the Rust application.
- `libs/hbb_common/src/config.rs`: Centralized configuration management.
