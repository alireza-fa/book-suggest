import uuid

from apps.authentication.models import UserAuth


class AuthenticationRepository:
    Model = UserAuth

    def check_user_auth_is_exist(self, user_id: int) -> bool:
        return self.Model.objects.only("id").filter(user_id=user_id).exists()

    def get_user_auth_by_user_id(self, user_id: int) -> Model:
        return self.Model.objects.get(user_id=user_id)

    def create_user_auth(self, user_id: int) -> Model:
        return self.Model.objects.create(
            user_id=user_id,
            access_uuid=uuid.uuid4(),
            refresh_uuid=uuid.uuid4(),
        )

    def update_user_auth_uuid(self, user_id: int) -> int:
        return self.Model.objects.filter(user_id=user_id).update(access_uuid=uuid.uuid4(), refresh_uuid=uuid.uuid4())


def get_authentication_repository():
    return AuthenticationRepository()
