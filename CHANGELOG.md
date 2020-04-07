# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## [Unreleased] - xxxx-xx-xx

### Added

### Changed

### Fixed

### Removed


## [v0.6.4] - 2020-04-07

### Added

- Implemented pytests fixture: 1 browser by session #143
- Check staled elements at control base, wip dev #143

### Changed

- Moved asserts to own class + add greater/lower_or_equals #279

### Fixed

### Removed

- Remove ControlForm and StrictRules + tests #305
- Enums and inherit classes #312
- Enum34 dependency just for >py34 versions #312


## [v0.6.3] - 2020-01-29

### Added
- New '__repr__' method for class 'StrictRule' #287
- Now 'ControlTable' support multiples tbodies #248
- Support for Python 3.7 after 20-01-2020 #298

### Changed
- Internal vars at controls packages moved to pythonic properties #287
- Clarify settings methods for controls,now is more readable #287
- Some WARN and ERR messages must be DEBUG messages #289
- Now exceptions group certain params+values+selenium when raises #289
- Refactor LoggerManager #290

### Fixed
- Tests execution failed after fresh install #293

### Removed
- Key from controls settings names 'instance' #287
- Support for Python 2.7 after 2020-01-01 #295


## [v0.6.2] - 2019-05-22

### Added

### Changed

### Fixed
- Can't load ControlTable si no existe un THEAD y existe TBODY #282
- Package build error after qacode==v0.6.0, urllib3<1.25 #280

### Removed
- Removed nosetest and nose-config support #280


## [v0.6.1] - 2019-04-20

### Added
- New module at 'qacode.core.loggers' named 'logger_messages' #untracked
- New nav_base method named ele_wait_value #untracked
- Move dropdown methods to new control dropdown class #258
- Added new class named 'ControlTable' #248
- Add coverage tests for function: driver_name_filter #268
- Add coverage tests for module : 'qacode.core.webs.strict_rules' #273

### Changed
- Separate benchmark test from all functional tests at tox -e coverage #251
- Moved log messages to new class to centralize them #untracked
- Refactor for control suites after changes from #247 , #untracked
- Updated USAGE.rst documentation #258
- Now get_text check for input tag #untracked
- Function with Cognitive Complexity of 13 (exceeds 5 allowed) #265
- New internal method to reduce duplication at ControlDropdown #untracked
- Fix similar code at #271
- Renamed settings_ methods to cfg_ #267

### Fixed
- Can't use dropdown methods if ControlForm strict_tags is disabled #247
- Some PageExceptions was failing at instantiation #untracked
- Now get_tag update self property
- Fixed CI complexity issue for #261
- Some ControlForm+inherit could fail if stric_rules was None #248

### Removed
- Deleted ControlGroup + tests #256
- Deleted controls property named 'on_instance_load' #259
- Deleted opera support #270

## [v0.6.0] - 2019-03-18

### Added
- Now controls can wait some webdriver conditions #242

### Changed
- Improve raises logging output #207

### Fixed
- find_child/find_children tests + some reload bugs #235
- Syntax error naming variable at controls.set_css_value #243

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


[Unreleased]: https://github.com/netzulo/qacode/compare/v0.6.4...HEAD
[0.6.4]: https://github.com/netzulo/qacode/compare/v0.6.3...v0.6.4
[0.6.3]: https://github.com/netzulo/qacode/compare/v0.6.2...v0.6.3
[0.6.2]: https://github.com/netzulo/qacode/compare/v0.6.1...v0.6.2
[0.6.1]: https://github.com/netzulo/qacode/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/netzulo/qacode/compare/v0.5.9...v0.6.0
[0.5.9]: https://github.com/netzulo/qacode/compare/v0.5.8...v0.5.9
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
