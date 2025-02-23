from app.models import User
from app.repositories import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def get_by_username(self, username):
        pass

    def get_by_email(self, email):
        pass

    def get_by_actor_id(self, actor_id):
        pass

    def get_verified_users(self):
        pass

    def get_users_by_visibility(self, visibility):
        pass

    def get_users_with_items(self):
        pass

    def get_active_lenders(self):
        pass

    def get_active_borrowers(self):
        pass

    def update_address(self, user_id, address):
        pass

    def verify_address(self, user_id):
        pass

    def update_profile_visibility(self, user_id, visibility):
        pass

    def search_users(self, query):
        pass
