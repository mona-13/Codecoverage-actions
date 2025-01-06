# This can be empty, or you can initialize things here if needed
from .addition import add  # Automatically expose `add` function when the package is imported

__all__ = ['add']  # Explicitly define the public interface of the package
