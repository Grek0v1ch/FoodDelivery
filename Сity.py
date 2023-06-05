# from dataclasses import dataclass, field
#
# from Area import Area
#
#
# @dataclass(frozen = True)
# class City:
#     areas: list[Area] = field(default_factory=lambda : []) [Area() for _ in range(3)]
#     matrix_areas_location: list[list[int]] = [[2], [2], [0, 1]]
