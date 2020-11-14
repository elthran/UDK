from expects import expect, have_keys


def test_api_users(client):
    """Start with a blank database."""

    user = client.get('/api/users/1').get_json()

    expect(user).to(have_keys(id=1, username='test_user'))


def test_api_counties(client):
    """Start with a blank database."""

    user = client.get('/api/counties/1').get_json()

    expect(user).to(have_keys({
        'county': {
            'background': 'Priest',
            'employedWorkers': 150,
            'gold': 750,
            'grainStores': 500,
            'happiness': 75,
            'happinessChange': 2,
            'healthiness': 75,
            'iron': 50,
            'land': 150,
            'leader': 'Test Leader',
            'mana': 0,
            'manaChange': 1,
            'maxMana': 10,
            'name': 'Test County',
            'population': 500,
            'productionChoice': 'Overwork',
            'race': 'Human',
            'rations': 1.0,
            'stone': 0,
            'taxRate': 7,
            'title': 'Sir',
            'wood': 250,
            'buildings': [
                {'className': 'Homestead',
                 'description': 'Each percent of land increases your '
                                'birth rate by 5%.',
                 'goldCost': 65,
                 'id': 1,
                 'stoneCost': 0,
                 'woodCost': 20},
                {'className': 'Wheat Field',
                 'description': 'Provides enough grain to feed 40 '
                                'people a day.',
                 'goldCost': 50,
                 'id': 2,
                 'stoneCost': 0,
                 'woodCost': 10},
                {'className': 'Dairy Farm',
                 'description': 'Produces enough food to feed 60 '
                                'people a day, but excess dairy is '
                                'lost each day.',
                 'goldCost': 75,
                 'id': 3,
                 'stoneCost': 0,
                 'woodCost': 20}
            ],
        }}))
