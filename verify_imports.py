
import os
import sys
import pkgutil
import importlib
import inspect
from pathlib import Path

def verify_package(package_name):
    print(f"Verifying package: {package_name}")
    try:
        package = importlib.import_module(package_name)
    except ImportError as e:
        print(f"FAILED to import package {package_name}: {e}")
        return False

    print(f"Successfully imported {package_name}")
    
    if hasattr(package, '__all__'):
        print(f"Checking __all__ in {package_name}")
        for item in package.__all__:
            if not hasattr(package, item):
                print(f"MISSING EXPORT: {item} in {package_name}")
                return False
            else:
                 print(f"  - {item}: OK")

    if hasattr(package, '__path__'):
        for _, name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
            print(f"Checking module: {name}")
            try:
                module = importlib.import_module(name)
                if hasattr(module, '__all__'):
                    for item in module.__all__:
                        if not hasattr(module, item):
                            print(f"MISSING EXPORT: {item} in {name}")
                            return False
                        # else:
                        #     print(f"  - {item}: OK")
            except ImportError as e:
                print(f"FAILED to import module {name}: {e}")
                return False
            except AttributeError as e:
                 print(f"FAILED to access attribute in module {name}: {e}")
                 return False
            except Exception as e:
                print(f"An unexpected error occurred in {name}: {e}")
                return False
                
    return True

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath("src"))
    if verify_package("promethium"):
        print("\nVERIFICATION SUCCESSFUL: All modules and exports are valid.")
        sys.exit(0)
    else:
        print("\nVERIFICATION FAILED")
        sys.exit(1)
