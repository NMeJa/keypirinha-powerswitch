import keypirinha as kp
import keypirinha_util as kpu
import os
import zipfile

class PowerUtility:
    """Utility class for common power management operations"""
    
    @staticmethod
    def extract_tools(plugin_instance):
        """Extract tools from package to cache directory"""
        try:
            cache_dir = plugin_instance.get_package_cache_path(create=True)
            tools_dir = os.path.join(cache_dir, "tools")
            psshutdown_path = os.path.join(tools_dir, "psshutdown64.exe")

            if not os.path.exists(psshutdown_path):
                os.makedirs(tools_dir, exist_ok=True)
                package_path = os.path.join(
                    kp.installed_package_dir(),
                    plugin_instance.package_full_name() + ".keypirinha-package"
                )
                
                with zipfile.ZipFile(package_path, 'r') as zip_ref:
                    for file in zip_ref.namelist():
                        if file.startswith('tools/'):
                            zip_ref.extract(file, cache_dir)

            return psshutdown_path

        except Exception as e:
            plugin_instance.err("Failed to extract tools:", str(e))
            return None

class PowerAction(kp.Plugin):
    """Base class for power management actions"""
    
    SECTION = "powerswitch"
    DEFAULT_ALIASES = []  # Override in child classes
    ICON_NAME = ""       # Override in child classes
    DESCRIPTION = ""     # Override in child classes
    COMMAND_ARG = ""     # Override in child classes

    def __init__(self):
        super().__init__()
        self._aliases = self.DEFAULT_ALIASES
        self._psshutdown_path = None

    def on_start(self):
        self._read_config()
        self.set_default_icon(self.load_icon(f"res://{self.package_full_name()}/{self.ICON_NAME}"))
        self._psshutdown_path = PowerUtility.extract_tools(self)
        self.on_catalog()

    def _read_config(self):
        settings = self.load_settings()
        action_name = self.__class__.__name__.lower()
        aliases_str = settings.get_stripped(f"{action_name}_aliases", self.SECTION)
        if aliases_str:
            self._aliases = [alias.strip() for alias in aliases_str.split(",")]

    def on_catalog(self):
        catalog = []
        for alias in self._aliases:
            catalog.append(self.create_item(
                category=kp.ItemCategory.KEYWORD,
                label=alias,
                short_desc=self.DESCRIPTION,
                target=self.__class__.__name__.lower(),
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.NOARGS
            ))
        self.set_catalog(catalog)

    def on_execute(self, item, action):
        if item.target() == self.__class__.__name__.lower():
            try:
                if not self._psshutdown_path or not os.path.exists(self._psshutdown_path):
                    self._psshutdown_path = PowerUtility.extract_tools(self)
                kpu.shell_execute(self._psshutdown_path, args=f"{self.COMMAND_ARG} -t 0")
            except Exception as e:
                self.err(f"Failed to execute {self.__class__.__name__.lower()} command:", str(e))

    def on_events(self, flags):
        if flags & kp.Events.PACKCONFIG:
            self._read_config()
            self.on_catalog()

class Sleep(PowerAction):
    DEFAULT_ALIASES = ["sleep"]
    ICON_NAME = "sleep.ico"
    DESCRIPTION = "Put Windows to sleep"
    COMMAND_ARG = "-d"

class Hibernate(PowerAction):
    DEFAULT_ALIASES = ["hibernate"]
    ICON_NAME = "hibernate.ico"
    DESCRIPTION = "Hibernate Windows"
    COMMAND_ARG = "-h"

class Lock(PowerAction):
    DEFAULT_ALIASES = ["lock"]
    ICON_NAME = "lock.ico"
    DESCRIPTION = "Lock Windows"
    COMMAND_ARG = "-l"

class Restart(PowerAction):
    DEFAULT_ALIASES = ["restart"]
    ICON_NAME = "reloading.ico"
    DESCRIPTION = "Restart Windows"
    COMMAND_ARG = "-r"

class Shutdown(PowerAction):
    DEFAULT_ALIASES = ["shutdown"]
    ICON_NAME = "power-on.ico"
    DESCRIPTION = "Shutdown Windows"
    COMMAND_ARG = "-s"
