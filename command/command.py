from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract class for implementing command pattern"""
    @abstractmethod
    def execute(self, book):
        pass
