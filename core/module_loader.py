import os
import json


class ModuleLoader:
    def __init__(self, app, db):
        self.__app = app
        self.__db = db

    # def __check_loadable(self, module):
    #     for mod in self.found_modules:
    #         # Check if scanned modules requires selected module
    #         if len(set(mod["REQUIRES"]).intersection_update(set(module["PROVIDES"]))) > 0:
    #             # Chck if selected module requires scanned module
    #             if len(set(module["REQUIRES"]).intersection_update(set(mod["PROVIDES"]))) > 0:
    #                 print("CIRCULAR DEPENDENCY ERROR")
    #                 return True
    #     return False

    @staticmethod
    def scan(pkgs_directory):
        # Scan the package directory and check for package.json
        packages = os.listdir(pkgs_directory)
        modules = {}
        for package in packages:
            print("Examining package:", package)
            package_meta_json = os.path.join(pkgs_directory, package, "package.json")
            try:
                package_meta = json.load(open(package_meta_json, "r"))
                if len(package_meta["PROVIDES"]) >= 1:
                    package_meta["PACKAGE_DIR"] = os.path.join(pkgs_directory, package)
                    for module in package_meta["PROVIDES"]:
                        if module not in modules:
                            modules[module] = package_meta
                        else:
                            print("Module already provided by another package")
                else:
                    print("Package should provide at least one module")
            except FileNotFoundError:
                print("Module does not contain package.json file")
            except json.JSONDecodeError:
                print("Malformed json meta file")

# TODO: Check if there are circular dependencies
# TODO: Create a sorted list of packages to load
# TODO: Function to get instance of module
