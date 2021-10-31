from locust import HttpUser, task

class AVSWebUser(HttpUser):
    @task
    def pressure_test(self):
        self.client.get("/")
        self.client.get("/login/")
        self.client.get("/register/client/")
        self.client.get("/register/conslutant/")