"""
Single Responsibility Principle
or Separate of Concerns Principle
"""


class Journal:
    """
    Journal class
    """

    def __init__(self) -> None:
        """
        Initialize Journal
        """
        self.entries: list[str] = []
        self.count: int = 0

    def add_entry(self, text: str) -> None:
        """
        Add entry to journal by text
        :param text: Data for new entry
        :type text: str
        :return: None
        :rtype: NoneType
        """
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos: int) -> None:
        """
        Remove entry by position index
        :param pos: position of entry
        :type pos: int
        :return: None
        :rtype: NoneType
        """
        del self.entries[pos]

    def __str__(self) -> str:
        return "\n".join(self.entries)

    # "Anti-pattern": God object where all functionality including:
    # crud, persistence, etc. goes into same class.

    # def save(self, filename: str):
    #     """
    #     Save the object class itself to a file
    #     :param filename: Name of the file
    #     :type filename: str
    #     :return: None
    #     :rtype: NoneType
    #     """
    #     with open(file=filename, mode='w', encoding='utf-8') as file:
    #         file.write(str(self))
    #         file.close()
    #
    # def load(self, filename: str):
    #     pass
    #
    # def low_from_web(self, uri: str):
    #     pass


class PersistenceManager:
    """
    Persistence Manager class
    """

    @staticmethod
    def save_to_file(journal: Journal, filename: str) -> None:
        """
        Save the object class itself to a file
        :param journal: Object to save
        :type journal: Journal
        :param filename: Name of the file
        :type filename: str
        :return: None
        :rtype: NoneType
        """
        with open(file=filename, mode="w", encoding="utf-8") as file:
            file.write(str(journal))
            file.close()

    @staticmethod
    def load(filename: str) -> None:
        """
        Load object from filename
        :param filename: Name of the file
        :type filename: str
        :return: None
        :rtype: NoneType
        """

    @staticmethod
    def load_from_web(uri: str) -> None:
        """
        Load data from URI
        :param uri: Web address to access object from the web
        :type uri: str
        :return: None
        :rtype: NoneType
        """


my_journal: Journal = Journal()
my_journal.add_entry("I cried today.")
my_journal.add_entry("I ate a bug.")
print(f"Journal entries:\n{my_journal}")
FILE: str = r"/data/journal.txt"
PersistenceManager.save_to_file(my_journal, FILE)
