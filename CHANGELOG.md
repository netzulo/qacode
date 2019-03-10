# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## [Unreleased] - xxxx-xx-xx

### Added

### Changed

### Fixed

### Removed


## [v0.5.9] - 2019-03-11

### Added
- Autodoc for package 'qacode.core.exceptions' #223
- Add find_child/s method + TCs #235

### Changed
- Improve Control Search #222
- Updated lib 'selenium' from 3.12.0 to 3.14.0 #228
- Now enum_base is being tested and documented #181
- Documentation now generated with bootstrap theme

### Fixed
- CI appveyor builds failing since tag v0.5.7 #226
- Failing setup.py install on python2.7 before next release #233


## [v0.5.8] - 2019-02-11

### Added
- This CHANGELOG
- MANIFEST.in
- Github pages at : https://netzulo.github.io

### Changed
- README.rst and USAGE.rst to v.5.4 changes
- Now controls can 'click' include when an element it's not visible or attached to DOM (this behaviour can be disabled)
- README.rst, included documentation urls
- Renamed class TlBase to ReporterTestlink #200

### Fixed
- tox envs to v0.5.4 changes (stop using qautils at setup.py)
- failing install because pytest haven't fixed version at setup.py #212
- tox environment to generate documentation #211
- click it's reloading an element when param retry=False #208
- class ControlGroup doesn't have reload call and no test #204
- page.get_elements was not parsing ControlGroup classes at calls #205
- py.test arguments calls working at root path while development #220

### Removed
- Old documentation files


[Unreleased]: https://github.com/netzulo/qacode/compare/v0.5.8...HEAD
[0.5.8]: https://github.com/netzulo/qacode/compare/v0.5.7...v0.5.8
[0.5.7]: https://github.com/netzulo/qacode/compare/v0.5.6...v0.5.7
[0.5.6]: https://github.com/netzulo/qacode/compare/v0.5.6...v0.5.6
[0.5.5]: https://github.com/netzulo/qacode/compare/v0.5.6...v0.5.5
[0.5.4]: https://github.com/netzulo/qacode/compare/v0.5.6...v0.5.4
[0.5.3]: https://github.com/netzulo/qacode/compare/v0.5.6...v0.5.3
[0.5.2]: https://github.com/netzulo/qacode/compare/v0.5.6...v0.5.2
[0.5.1]: https://github.com/netzulo/qacode/compare/v0.4.6...v0.5.1
[0.5.0]: https://github.com/netzulo/qacode/compare/v0.4.6...v0.5.0
[0.4.8]: https://github.com/netzulo/qacode/compare/v0.4.8...v0.4.9
[0.4.7]: https://github.com/netzulo/qacode/compare/v0.4.6...v0.4.7
[0.4.6]: https://github.com/netzulo/qacode/compare/v0.4.5...v0.4.6
[0.4.5]: https://github.com/netzulo/qacode/compare/v0.4.4...v0.4.5
[0.4.4]: https://github.com/netzulo/qacode/compare/v0.4.3...v0.4.4
[0.4.3]: https://github.com/netzulo/qacode/compare/v0.4.2...v0.4.3
[0.4.2]: https://github.com/netzulo/qacode/compare/v0.4.1...v0.4.2
[0.4.1rc-a]: https://github.com/netzulo/qacode/compare/v0.4.1...v0.4.1rc-a
[0.4.1]: https://github.com/netzulo/qacode/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/netzulo/qacode/compare/v0.3.9rc-a...v0.4.0
[0.3.9rc-a]: https://github.com/netzulo/qacode/compare/v0.3.9...v0.3.9rc-a
[0.3.9]: https://github.com/netzulo/qacode/compare/v0.3.8rc-c...v0.3.9
[0.3.8rc-c]: https://github.com/netzulo/qacode/compare/v0.3.8rc-b...v0.3.8rc-c
[0.3.8rc-b]: https://github.com/netzulo/qacode/compare/v0.3.8rc-a...v0.3.8rc-b
[0.3.8rc-a]: https://github.com/netzulo/qacode/compare/v0.3.8...v0.3.8rc-a
[0.3.8]: https://github.com/netzulo/qacode/compare/v0.3.7...v0.3.8
[0.3.7]: https://github.com/netzulo/qacode/compare/v0.3.6...v0.3.7
[0.3.6]: https://github.com/netzulo/qacode/compare/v0.3.5...v0.3.6
[0.3.5]: https://github.com/netzulo/qacode/compare/v0.3.4...v0.3.5
[0.3.4]: https://github.com/netzulo/qacode/compare/v0.3.3...v0.3.4
[0.3.3]: https://github.com/netzulo/qacode/compare/v0.3.2...v0.3.3
[0.3.2]: https://github.com/netzulo/qacode/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/netzulo/qacode/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/netzulo/qacode/compare/v0.2.9...v0.3.0
[0.2.9]: https://github.com/netzulo/qacode/compare/v0.2.8...v0.2.9
[0.2.8]: https://github.com/netzulo/qacode/compare/v0.2.7...v0.2.8
[0.2.7]: https://github.com/netzulo/qacode/compare/v0.2.6...v0.2.7
[0.2.6]: https://github.com/netzulo/qacode/compare/v0.2.5...v0.2.6
[0.2.5]: https://github.com/netzulo/qacode/compare/v0.2.4...v0.2.5
[0.2.4]: https://github.com/netzulo/qacode/compare/v0.2.3...v0.2.4
[0.2.3]: https://github.com/netzulo/qacode/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/netzulo/qacode/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/netzulo/qacode/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/netzulo/qacode/compare/v0.1.9...v0.1.0
[0.1.9]: https://github.com/netzulo/qacode/compare/v0.1.8...v0.1.9
[0.1.8]: https://github.com/netzulo/qacode/compare/v0.1.7...v0.1.8
[0.1.7]: https://github.com/netzulo/qacode/compare/v0.1.6...v0.1.7
[0.1.6]: https://github.com/netzulo/qacode/compare/v0.1.5...v0.1.6
[0.1.5]: https://github.com/netzulo/qacode/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/netzulo/qacode/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/netzulo/qacode/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/netzulo/qacode/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/netzulo/qacode/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/netzulo/qacode/compare/v0.0.9...v0.1.0
[0.0.9]: https://github.com/netzulo/qacode/compare/v0.0.8...v0.0.9
[0.0.8]: https://github.com/netzulo/qacode/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/netzulo/qacode/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/netzulo/qacode/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/netzulo/qacode/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/netzulo/qacode/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/netzulo/qacode/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/netzulo/qacode/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/netzulo/qacode/compare/v0.0.0...v0.0.1
