from app.serializers.base_serializer import BaseSerializer

from app.serializers.county_serializer import CountySerializer


class KingdomSerializer(BaseSerializer):
    def __init__(self, kingdom, view=None):
        super().__init__(kingdom, view=view)
        self.fields("id", "name", counties=CountySerializer.call(kingdom.counties))
