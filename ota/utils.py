import hashlib


def search_for_prop(buildprop, prop):
    for prop_to_check in buildprop:
        current_prop = prop_to_check.split("=")

        if current_prop[0] == prop:
            return current_prop[1]

    return None


def clean_buildprop(buildprop):
    buildprop_array = buildprop.split('\n')

    intermediate_buildprop = list(filter(lambda x: x != '', buildprop_array))
    new_buildprop = list(filter(
        lambda x: not(x.startswith('#')), intermediate_buildprop))

    return new_buildprop


def calculate_md5(file):
    if not file:
        return None
    md5 = hashlib.md5()
    for chunk in file.chunks():
        md5.update(chunk)
    return md5.hexdigest()
