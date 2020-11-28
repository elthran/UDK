from app.serializers.base_serializer import BaseSerializer


class BuildingSerializer(BaseSerializer):
    def __init__(self, building):
        super().__init__(building)
        self.fields(
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
