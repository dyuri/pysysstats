import psutil


def get_stat():
    virtual = psutil.virtual_memory()
    swap = psutil.swap_memory()

    meta = {
    }
    stats = {
        "virtual": {
            "total": virtual.total,
            "available": virtual.available,
            "percent": virtual.percent,
            "free": virtual.free,
            "active": virtual.active,
            "inactive": virtual.inactive,
            "buffers": virtual.buffers,
            "cached": virtual.cached,
            "shared": virtual.shared,
        },
        "swap": {
            "total": swap.total,
            "used": swap.used,
            "free": swap.free,
            "percent": swap.percent,
            "sin": swap.sin,
            "sout": swap.sout,
        },
    }

    return {
        "name": "memory",
        "meta": meta,
        "stats": stats,
    }
