# Defined in csrc/ass.cpp

class Ass:
    def __init__(self,
                 width: int,
                 height: int,
                 reserve_blank: int = 0,
                 font_face: str = "sans-serif",
                 font_size: float = 25.0,
                 alpha: float = 1.0,
                 duration_marquee: float = 5.0,
                 duration_still: float = 5.0,
                 filter: str = "",
                 reduced: bool = False,
                 bold: bool = False,
                 live: bool = False,
                ): ...

    def add_comment(self, progress: float, ctime: int, content: str, size_factor: float, mode: int, color: int, pool: int) -> bool:
        """add a comment to Ass object, return True if add success"""
        ...

    def add_nico_comment(self, progress: float, duration: float, ctime: int, content: str, font_size: float, mode: int, color: int,
                        alpha_factor: float, font: str, pool: int, full: bool, ender: bool) -> bool:
        """add a niconico-style comment to Ass object, return True if add success"""
        ...

    def to_string(self) -> str:
        """return the ass text"""
        ...

    def write_to_file(self, str) -> None:
        """direct write to the file to avoid memory cost"""
