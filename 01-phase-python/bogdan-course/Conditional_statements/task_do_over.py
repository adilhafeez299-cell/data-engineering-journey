def route_info (route_dict:dict):
    if "distance" in route_dict and isinstance(route_dict["distance"], int):
        return f"distance to you destination is {route_dict['distance']}"
    elif "speed" in route_dict and "time" in route_dict:
        return f"distance to your destination is {route_dict['speed'] * route_dict['time']}"
    return "No distance info is available"

print(route_info({"distance": 100}))
print(route_info({"speed": 50, "time": 2}))
print(route_info({"invalid": "data"}))