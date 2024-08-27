from sqlalchemy.orm import Session


class FakeSession(Session):
    committed: bool = False

    def commit(self,) -> None:
        self.committed = True

