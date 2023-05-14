from PKViewsData.PKViewsDataProtocol import PKViewsDataProtocol
from PKViewRules.PKViewRules import PKViewRules

from dataclasses import dataclass
from typing import List



@dataclass
class PKViewsData(PKViewsDataProtocol):
    views_rules: List[PKViewRules]
    
    def serialize(self) -> dict:
        views_rules= []

        for view_rules in self.views_rules:
            data_item = {}
            data_item['id'] = view_rules.id
            data_item['view_type'] = view_rules.view_type
            data_item['layout_config'] = view_rules.layout_config
            if view_rules.visual_properties:
                data_item['visual_properties'] = view_rules.visual_properties
            if view_rules.visual_effects:
                data_item['visual_effects'] = view_rules.visual_effects
            
            views_rules.append(data_item)

        return {
            'views_rules': views_rules
        }