def searchForProp(buildprop, prop):
    buildprop_array = cleanBuildProp(buildprop)
    
    for prop_to_check in buildprop_array:
        current_prop = prop_to_check.split("=")
        if current_prop[0] == prop:
            return current_prop[1]
    
    return "No prop found"

def cleanBuildProp(buildprop):
    buildprop_array = buildprop.split('\n')

    intermediate_buildprop = list(filter(lambda x : x != '', buildprop_array))
    new_buildprop = list(filter(lambda x : not(x.startswith('#')), intermediate_buildprop))

    #for prop in buildprop_array:
    #    if (prop == "") or (prop.startswith("# ")):
    #        print("oh no")
    #        buildprop_array.remove(prop)
    #        print(buildprop_array)
    
    return new_buildprop
            