from app.serializers.base_serializer import BaseSerializer


class UnitSerializer(BaseSerializer):
    def __init__(self, unit):
        super().__init__(unit)
        self.fields(
            "id",
            "class_name",
            "class_name_plural",
            "total_owned",
            "gold_cost",
            "wood_cost",
            "iron_cost",
            "upkeep",
            "attack",
            "defence",
            "health",
            "category",
            "armour",
            "description",
            available=unit.get_available(),
        )
