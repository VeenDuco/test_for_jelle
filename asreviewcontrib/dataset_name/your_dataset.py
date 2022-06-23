from asreview.datasets import BaseDataSet
from asreview.datasets import BaseDataGroup
from pathlib import Path


class example_dataset_local(BaseDataSet):
    """
    This is an example dataset that is stored locally.
    """

    import os
    __filepath__ = os.getcwd()

    def __init__(self):
        super().__init__(
            dataset_id="test_voor_jelle",
            filepath=str(Path(self.__filepath__, 'data', 'your_dataset.csv')),
            title="Dataset template test voor jelle",
            description="This is an example dataset that is stored locally.",
            authors="Veen, D.",
            topic="A test case",
            link=None,
            reference=None,
            img_url=None,
            license=None,
            year="2023"
        )


