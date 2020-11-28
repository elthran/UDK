from app.serializers.base_serializer import BaseSerializer
from app.serializers.unit_serializer import UnitSerializer
from app.serializers.building_serializer import BuildingSerializer


class CountySerializer(BaseSerializer):
    def __init__(self, county, view=None):
        super().__init__(county, view=view)
        self.fields(
            "id",
            "name",
            "leader",
            "title",
            "race",
            land=county.economy.land,
        )

    def full_view(self, county):
        self.add_fields(
            "day",
            "background",
            population=county.economy.population,
            defensive_power=county.military.defensive_power(),
            happiness=75,
            happiness_change=2,
            healthiness=county.economy.healthiness,
            land=county.economy.land,
            gold=county.economy.gold,
            wood=county.economy.wood,
            iron=county.economy.iron,
            stone=county.economy.stone,
            mana=county.economy.mana,
            max_mana=10,
            mana_change=1,
            offensive_power=county.military.offensive_power(),
            units=UnitSerializer.call(county.military.units),
            buildings=BuildingSerializer.call(county.infrastructure.buildings),
            employed_workers=county.infrastructure.get_employed_workers(),
            grain_stores=county.economy.grain_stores,
            tax_rate=county.preference._tax_rate,
            rations=county.preference.rations,
            production_choice=county.preference.production_choice,
        )
