from fastapi import APIRouter
import pkgutil
import importlib
main_router = APIRouter()

package = __name__
modules = (importlib.import_module(f"{package}.{name}") for _, name, _ in pkgutil.iter_modules(__path__))

for module in modules:
    if hasattr(module, "router"):
        main_router.include_router(module.router)