from user_dao import UserDAO

from user import User


class UserController:
    def __init__(self) -> None:
        pass

    def get_all(self) -> User:
        user = UserDAO.get_instance().get_all()
        return user
    
