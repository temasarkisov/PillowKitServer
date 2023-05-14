from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class PKViewRules:
    id: str
    view_type: str
    layout_config: Dict[str, str]
    visual_properties: Optional[Dict[str, str]]
    visual_effects: Optional[Dict[str, str]]