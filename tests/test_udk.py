def test_empty_db(client):
    """Start with a blank database."""

    user = client.get('/api/users/1').get_json()

    expect(user).to(have_keys(id=1, username='test_user'))
