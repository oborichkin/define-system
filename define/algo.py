from typing import List


class Step:
    def __init__(self, text=None):
        self.text: str = text
        self.substeps: List[Step] = []

    def __html__(self):
        html = ""
        if self.text:
            html += f"<li>{self.text}</li>"
        if self.substeps:
            html += f"<ol>{''.join([step.__html__() for step in self.substeps])}</ol>"
        return html

    @property
    def html(self):
        return self.__html__()
