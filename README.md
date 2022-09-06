# Rez `make` package for Windows
[Rez](https://github.com/AcademySoftwareFoundation/rez) package for the gnu make utility.

## Requirements 📦

- [rez](https://github.com/AcademySoftwareFoundation/rez)
- [make](https://osdn.net/projects/sfnet_ezwinports/downloads/make-4.3-without-guile-w32-bin.zip/) zip archive

## Building 🔨

- Fork this repo
- Download [make](https://osdn.net/projects/sfnet_ezwinports/downloads/make-4.3-without-guile-w32-bin.zip/) zip archive for Windows from the internet and place in `rel/`
- Build

```sh
rez build -i
```

## Release 🚢

- Set `SYSTEM_REZ_EXTERNAL_PACKAGES` in your environment or remove / edit the block below in package.py so that it points to the default or desired release path respectively.

```python
with scope('config') as config:
    config.release_packages_path = '${SYSTEM_REZ_EXTERNAL_PACKAGES}'
```

- If changing package.py is necessary then git commit and push that code before releasing, otherwise it's as simple as:

```sh
rez release -m "Initial release"
```
