from PKViewRules.PKViewRules import PKViewRules
from PKUtils.JSON_manager import load_JSON

from typing import Dict


class PKViewRulesBuilder:
    def build(
        self,
        view_id, 
        view_data: Dict
    ) -> PKViewRules:
        view_type = view_data['view_type']
        layout_config = view_data['layout_config']
        if 'visual_properties' in view_data:
            visual_properties = view_data['visual_properties']
        else:
            visual_properties = None
        if 'visual_effects' in view_data:
            visual_effects = view_data['visual_effects']
        else:
            visual_effects = None

        return PKViewRules(
            id=view_id,
            view_type=view_type,
            layout_config=layout_config,
            visual_properties=visual_properties,
            visual_effects=visual_effects,
        )