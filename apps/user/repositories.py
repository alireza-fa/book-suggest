from django.contrib.auth import get_user_model


class UserRepository:
    Op = "user.repositories.UserRepository."
    Model = get_user_model()

    def check_user_is_exist_by_username(self, username: str) -> bool:
        return self.Model.objects.only("id").filter(username=username).exists()

    def get_user_by_user_name(self, username: str):
        return self.Model.objects.get(username=username)

    def register_user(self, username: str, password: str):
        return self.Model.objects.create_user(username=username, password=password)


def get_user_repository():
    return UserRepository()
