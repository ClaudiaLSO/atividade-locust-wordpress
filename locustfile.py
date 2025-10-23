from locust import HttpUser, task, between

class WordPressUser(HttpUser):
    """
    Esta classe simula o comportamento de um utilizador a navegar
    nos 3 posts que criámos para os cenários de teste.
    """
    
    # Simula um utilizador real, que espera entre 1 e 3 segundos
    # antes de carregar a próxima página.
    wait_time = between(1, 3)

    @task # A anotação @task define uma ação do utilizador.
    def visit_post_1mb(self):
        """
        Tarefa para visitar o cenário 1: Post com imagem de 1MB
        """
        # Usamos o caminho relativo. O "host" (http://localhost)
        # será definido na interface do Locust.
        self.client.get("/2025/10/22/teste-imagem-1mb/", name="Post 1MB")

    @task
    def visit_post_400kb(self):
        """
        Tarefa para visitar o cenário 2: Post com texto de 400KB
        """
        self.client.get("/2025/10/22/texto-longo/", name="Post 400KB Texto")

    @task
    def visit_post_300kb(self):
        """
        Tarefa para visitar o cenário 3: Post com imagem de 300KB
        """
        self.client.get("/2025/10/22/imagem-media/", name="Post 300KB")