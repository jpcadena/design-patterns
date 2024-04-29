"""
Virtual Proxy script
"""

from typing import Optional, Union


class Bitmap:
    """
    Bitmap class
    """

    def __init__(self, filename: str):
        self.filename: str = filename
        print(f"Loading image from {self.filename}")

    def draw(self) -> None:
        """
        Draw the bitmap
        :return:None
        :rtype: NoneType
        """
        print(f"Drawing image {self.filename}")


class LazyBitmap:
    """
    Lazy Bitmap class
    """

    def __init__(self, filename: str):
        self.filename: str = filename
        self._bitmap: Optional[Bitmap] = None

    def draw(self) -> None:
        """
        Draw the bitmap
        :return:None
        :rtype: NoneType
        """
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image: Union[Bitmap, LazyBitmap]) -> None:
    """
    Draw image
    :param image: The image to draw
    :type image: Bitmap or LazyBitmap
    :return:None
    :rtype: NoneType
    """
    print("About to draw image")
    image.draw()
    print("Done drawing image")


if __name__ == "__main__":
    # bitmap: Bitmap = Bitmap("facepalm.jpg")
    # draw_image(bitmap)
    lazy_bitmap = LazyBitmap("facepalm.jpg")
    draw_image(lazy_bitmap)
