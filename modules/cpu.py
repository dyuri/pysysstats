import psutil


def get_stat():
    meta = {
        "count_logical": psutil.cpu_count(logical=True),
        "count_physical": psutil.cpu_count(logical=False),
    }
    stats = {
        "usage": psutil.cpu_percent(percpu=True),
        "freq": [{
            "current": f.current,
            "min": f.min,
            "max": f.max,
        } for f in psutil.cpu_freq(percpu=True)],
    }

    return {
        "name": "cpu",
        "meta": meta,
        "stats": stats,
    }
