import psutil


def get_usage(mp):
    usage = psutil.disk_usage(mp)

    return {
        "mountpoint": mp,
        "total": usage.total,
        "used": usage.used,
        "free": usage.free,
        "percent": usage.percent,
    }


def get_stat():
    partitions = psutil.disk_partitions()

    meta = {
        "partitions": [{
            "device": p.device,
            "mountpoint": p.mountpoint,
            "fstype": p.fstype,
            "opts": p.opts,
        } for p in partitions]
    }
    stats = {
        "usage": [get_usage(p.mountpoint) for p in partitions]
    }

    return {
        "name": "disk",
        "meta": meta,
        "stats": stats,
    }
