from locust import HttpUser, between, task
memory_hog = []
class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def allocate_memory(self):
        # Создаём большой массив (~1MiB за итерацию)
        memory_hog.append("x" * 1024 * 1024)
        # Можно также делать HTTP-запрос к приложению
        self.client.get("/")