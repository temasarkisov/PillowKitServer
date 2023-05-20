from PKViewsData.PKViewsDataProtocol import PKViewsDataProtocol
from PKViewRulesBuilder.PKViewRulesBuilder import PKViewRulesBuilder
from PKViewRules.PKViewRules import PKViewRules

from dataclasses import dataclass
from typing import List, Dict


class PKViewsData(PKViewsDataProtocol):
    views_rules: List[PKViewRules] = []
    view_rules_builder: PKViewRulesBuilder

    def __init__(
        self, 
        view_rules_builder
    ) -> None:
        super().__init__()
        self.view_rules_builder = view_rules_builder

    def make_view_rules(
        self, 
        views_rules: Dict,
    ) -> None:
        self.views_rules = []
        for view_id in views_rules:
            self.views_rules.append(
                self.view_rules_builder.build(
                    view_id=view_id,
                    view_data=views_rules[view_id]
                )
            )

    def serialize(self) -> Dict:
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