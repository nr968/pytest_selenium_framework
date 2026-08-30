def dict2class(d):
    if isinstance(d, list):
        return [dict2class(x) for x in d]
    if isinstance(d, tuple):
        return tuple(dict2class(x) for x in d)
    if not isinstance(d, dict):
        return d

    class C:
        pass

    obj = C()
    for key, value in d.items():
        setattr(obj, key.lower().replace(" ","_"), dict2class(value))
    return obj