from locust import HttpUser, task, between

class MLGatewayUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_prediction_endpoint(self):
        payload = {
            "full_name": "Saurabh",
            "email": "saurabh@mle.com",
            "github_profile": "https://github.com/saurabh"
        }
        self.client.post("/register-candidate", json=payload)