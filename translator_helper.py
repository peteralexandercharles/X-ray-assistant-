
w = "BONE AGE"
w = w.lower().strip().replace(" ", "_").replace("-","_").replace("X-RAY", "")
w = 'tp_' + w
print(w)

if 'right' in w:
    w = w.replace('right', 'left')
    print(w)
