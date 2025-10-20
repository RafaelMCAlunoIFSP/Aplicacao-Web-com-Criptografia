import importlib
import os
import pkgutil

def load_models(package_name: str):
    package = importlib.import_module(package_name)
    
    for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
        if not is_pkg:
            full_module_name = f"{package_name}.{module_name}"
            importlib.import_module(full_module_name)