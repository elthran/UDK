from expects import expect, have_keys, contain

from app.models.users import User


class TestApiCountiesController:
    def test_get_county_for_currrent_user(self, client, login):
        """Return the county view of the current user."""

        user = User.query.get(1)
        county = user.county
        login(user.username)

        data = client.get(f"/api/counties/{county.id}").get_json()

        expect(data["county"]).to(
            have_keys(
                {
                    "background": "Priest",
                    "employedWorkers": 150,
                    "gold": 750,
                    "grainStores": 500,
                    "happiness": 75,
                    "happinessChange": 2,
                    "healthiness": 75,
                    "iron": 50,
                    "land": 150,
                    "leader": "Test Leader",
                    "mana": 0,
                    "manaChange": 1,
                    "maxMana": 10,
                    "name": "Test County",
                    "population": 500,
                    "productionChoice": "Overwork",
                    "race": "Human",
                    "rations": 1.0,
                    "stone": 0,
                    "taxRate": 7,
                    "title": "Sir",
                    "wood": 250,
                    "buildings": contain(
                        have_keys(
                            {
                                "className": "Homestead",
                                "description": "Each percent of land increases your "
                                "birth rate by 5%.",
                                "goldCost": 65,
                                "id": 1,
                                "stoneCost": 0,
                                "woodCost": 20,
                            }
                        ),
                        have_keys(
                            {
                                "className": "Wheat Field",
                                "description": "Provides enough grain to feed 40 "
                                "people a day.",
                                "goldCost": 50,
                                "id": 2,
                                "stoneCost": 0,
                                "woodCost": 10,
                            }
                        ),
                        have_keys(
                            {
                                "className": "Dairy Farm",
                                "description": "Produces enough food to feed 60 "
                                "people a day, but excess dairy is "
                                "lost each day.",
                                "goldCost": 75,
                                "id": 3,
                                "stoneCost": 0,
                                "woodCost": 20,
                            }
                        ),
                    ),
                }
            )
        )

    def test_get_county_for_other_user(self, client, login):
        """Return the county view you get when viewing another user."""

        user1 = User.query.get(1)
        user2 = User.query.get(2)
        county2 = user2.county
        login(user1.username)

        data = client.get(f"/api/counties/{county2.id}").get_json()

        expect(data["county"]).to(
            have_keys(
                {
                    "id": 2,
                    "land": 150,
                    "leader": "Mechazoid",
                    "name": "Mechland",
                    "race": "Human",
                    "title": "Sir",
                }
            )
        )
