from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    name: Optional[str] = None
    price: Optional[float] = None
    weight: Optional[int] = None
    composition: Optional[str] = None
