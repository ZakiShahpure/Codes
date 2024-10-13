string = "Endless dreams, with a lot of dreams"
prefix = "Endless"                              #case sensitive
suffix = "dreams"
print(string.startswith(prefix))                #and if we want to check same thing for prefix, put endswith(suffix)
print(string.endswith(suffix))