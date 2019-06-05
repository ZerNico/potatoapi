def searchForProp(buildprop, prop):

    print("Also: " + str(type(buildprop)))
    
    for prop_to_check in buildprop:
        current_prop = prop_to_check.split("=")
        
        if current_prop[0] == prop:
            return current_prop[1]
    
    return None

def cleanBuildProp(buildprop):
    buildprop_array = buildprop.split('\n')

    intermediate_buildprop = list(filter(lambda x : x != '', buildprop_array))
    new_buildprop = list(filter(lambda x : not(x.startswith('#')), intermediate_buildprop))
    
    return new_buildprop
            
