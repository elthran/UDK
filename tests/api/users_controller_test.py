from expects import expect, have_keys


class TestApiUsersController:
    def test_get_user(self, client):
        """Start with a blank database."""

        data = client.get("/api/users/1").get_json()

        expect(data["user"]).to(have_keys(id=1, username="test_user"))
