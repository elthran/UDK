from app.serializers.base_serializer import BaseSerializer, fields, field


class BuildingSerializer(BaseSerializer):
    _fields = fields(
        "id",
        "class_name",
        "class_name_plural",
        "total_owned",
        "gold_cost",
        "wood_cost",
        "stone_cost",
        "output",
        "worker_capacity",
        "description",
    )
