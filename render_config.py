worlds["survival"] = "/home/broyojo/tmp/world"
processes = 4

def signFilter(poi):
    if poi['id'] == "Sign" or poi["id"] == "minecraft:sign":
        data = poi["Text1"] + poi["Text2"] + poi["Text3"] + poi["Text4"]
        if len(data) >= 2:
            if data[0] == data[-1] == "*":
                print("found marker")
                print(data)
                args = data.split(";")
                hover, text = "", ""
                for arg in args:
                    arg = arg.strip().strip("*")
                    ident, val = "", ""
                    try:
                        ident, val = arg.split(":")
                    except:
                        return None
                    if ident == "i":
                        print(val)
                        poi["icon"] = f"custom_icons/{val}.png"
                    elif ident == "t":
                        text = val
                    elif ident == "h":
                        hover = val
                    else:
                        print(f"unknown identifier {ident}")
                print("hover:", hover)
                print("text:", text)
                return (hover, text)

renders["survivalday"] = {
    "world": "survival",
    "title": "Overworld",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    # "crop": (-10000, -10000, 10000, 10000),
    "markers": [dict(name="Markers", filterFunction=signFilter)],
}

renders["survivalnether"] = {
    "world": "survival",
    "title": "Nether",
    "rendermode": normal,
    "dimension": "nether",
    # "crop": (-1250, -1250, 1250, 1250),
    "markers": [dict(name="Markers", filterFunction=signFilter)],
}

renders["survivalend"] = {
    "world": "survival",
    "title": "End",
    "rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.5)],
    "dimension": "end",
    "markers": [dict(name="Markers", filterFunction=signFilter)],
}

customwebassets = "/home/broyojo/webserver/custom_icons"
outputdir = "/home/broyojo/webserver/render"
