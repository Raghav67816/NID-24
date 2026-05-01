refs = {}
features = ["RMS", "STD DEV"]

def register_feature_calc(name):
    def decorator(func):
        if name not in features:
            print("invalid feature")
        else:
            refs[name] = func
        return func  # Return the function so it remains callable
    return decorator

@register_feature_calc("abc")
def calc_rms(x):
    return x + 1

print(calc_rms(1))
print(refs)
