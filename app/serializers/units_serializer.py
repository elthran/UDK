from app.serializers.base_serializer import BaseSerializer, fields, field


class UnitsSerializer(BaseSerializer):
    _fields = fields(
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
    )

    _fields.append(field("available", getter=lambda unit: unit.get_available()))
