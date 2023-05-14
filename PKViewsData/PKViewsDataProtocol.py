import abc


class PKViewsDataProtocol:
    @abc.abstractmethod
    def serialize(self) -> dict:
        pass