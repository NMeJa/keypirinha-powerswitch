# PowerSwitch Plugin for Keypirinha

A plugin for [Keypirinha](http://keypirinha.com) launcher to control Windows power states including sleep, hibernate, lock, restart, and shutdown.

## Features

* 🔌 Shutdown Windows (bye-bye!)
* 🔄 Restart Windows (turn it off and on again)
* 😴 Put Windows to Sleep (nap time!)
* ❄️ Hibernate Windows (deep sleep mode)
* 🔒 Lock Windows (keep it safe)
* ⚙️ Customizable aliases for each command
* 🎨 Icon indicators for each action

## Dependencies

This plugin uses PsShutdown64 from Windows Sysinternals Suite. The executable is included in the package.

## Installation

### Automatic
* Download the `PowerSwitch.keypirinha-package` from the releases
* Install it in Keypirinha using:
  * Drag and drop the package into Keypirinha
  * Or move it to: `%APPDATA%\Keypirinha\InstalledPackages\`

### Manual
1. Create a new folder `PowerSwitch` in `%APPDATA%\Keypirinha\Packages`
2. Copy all files from this repository into the new folder
3. Restart Keypirinha

## Configuration

The plugin can be configured by editing the `powerswitch.ini` file. You can access it through:
* Keypirinha's configuration panel: `Keypirinha → Configure → Apps → PowerSwitch`
* Or directly edit: `%APPDATA%\Keypirinha\Packages\PowerSwitch\powerswitch.ini`

### Default Configuration
```ini
[powerswitch]
# Command aliases (comma-separated)
shutdown_aliases = shutdown, poweroff, off
restart_aliases = restart, reboot
sleep_aliases = sleep, suspend
hibernate_aliases = hibernate, hiber
lock_aliases = lock, lockpc
```

## Usage

Type any of the configured aliases in Keypirinha to trigger the corresponding power action:
* `shutdown` - Shutdown Windows
* `restart` - Restart Windows
* `sleep` - Put Windows to sleep
* `hibernate` - Hibernate Windows
* `lock` - Lock Windows

Or use your custom aliases as configured in the .ini file.

## Credits

* [Keypirinha](http://keypirinha.com/) by Jean-Charles Lefebvre
* [PsShutdown](https://learn.microsoft.com/en-us/sysinternals/downloads/psshutdown) from Windows Sysinternals by Mark Russinovich

## License

This package is distributed under the terms of the MIT license.

## Version History

### v1.0
* Initial release
* Basic power management commands
* Customizable aliases
* Included PsShutdown64 utility

## Contributing

Feel free to contribute to this project by:
* Reporting bugs
* Suggesting enhancements
* Creating pull requests

## Notes

* Some commands may require administrative privileges
* The plugin creates a cache folder to store the PsShutdown64 executable
* Actions are executed immediately without confirmation prompts
* Make sure your work is saved before using shutdown or restart commands

![GitHub release (latest by date)](https://img.shields.io/github/v/release/YOUR-USERNAME/keypirinha-powerswitch)
![GitHub](https://img.shields.io/github/license/YOUR-USERNAME/keypirinha-powerswitch)
![GitHub all releases](https://img.shields.io/github/downloads/YOUR-USERNAME/keypirinha-powerswitch/total)
