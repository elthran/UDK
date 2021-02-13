from expects import expect, have_keys, equal


class TestApiAuthenticationController:
    def test_login(self, client):
        data = client.post(
            "/api/authentication/login",
            json=dict(username="test_user"),
            follow_redirects=True,
        ).get_json()
        expect(data["user"]).to(
            have_keys({"countyId": 1, "id": 1, "username": "test_user"})
        )

    def test_logout(self, client):
        data = client.post(
            "/api/authentication/logout",
            follow_redirects=True,
        ).get_json()
        expect(data["message"]).to(equal("Logout successful."))
