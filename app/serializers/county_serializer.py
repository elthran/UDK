from app.serializers.base_serializer import BaseSerializer
from app.serializers.preference_serializer import PreferenceSerializer


class CountySerializer(BaseSerializer):
    """docstring for CountySerializer"""

    @classmethod
    def render(cls, county, with_preference=False):
        data = {}

        fields = [
            'name',
            'leader',
            'day',
            'race',
            'title',
            'background',
            'weather'
        ]

        for key in fields:
            data[key] = getattr(county, key)

        if with_preference:
            data['preference'] = PreferenceSerializer.render(county.preference)

        # data['economy'] = EconomySerializer(county.economy).render()
        # data['infrastructure'] = InfrastructureSerializer(county.infrastructure).render()

        return data
