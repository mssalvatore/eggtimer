# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to
the [PEP 440 version scheme](https://peps.python.org/pep-0440/#version-scheme).

## [1.3.0] - 2024-01-24
### Changed
- The package name from `egg_timer` to `eggtimer`
- Deprecated the `egg_timer` package

## [1.2.0] - 2023-03-28
### Added
- ThreadSafeEggTimer
- A license section to README.md

### Changed
- Some verbiage in README.md


## [1.1.1] - 2023-02-16
### Fixed
- A bug where incorrect units resulted in a total malfunction of EggTimer.


## [1.1.0] - 2023-01-05
### Changed
- Use time.monotonic_ns() instead of time.time()


## [1.0.1] - 2022-10-14
### Added
- Support for type hinting


## [1.0.0] - 2022-09-04
### Added
- EggTimer
- Unit tests
- README.md
