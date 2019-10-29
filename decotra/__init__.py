from datetime import datetime as __dt


from decotra.s3 import track, path


def __o_add(num: int):
    """9->09 formatter"""
    return str(num) if num > 9 else f"0{num}"


__version__ = "0.0.4-dev"

__d = __dt.now()
saved_prefix = f"{__o_add(__d.year)}-{__o_add(__d.month)}-{__o_add(__d.day)}-{__o_add(__d.hour)}-{__o_add(__d.minute)}/"
