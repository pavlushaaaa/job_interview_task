class Route():
    def __init__(self, a, b, stops, distance):
        self.a = str(a)
        self.b = str(b)
        self.stops = int(stops)
        self.distance = int(distance)
    def __repr__(self):
        return f"A : {self.a} - B : {self.b}, stops : {self.stops}, distance : {self.distance}"


def func1(listt, num):
    num_of_routes = 0
    for i in listt:
        if i.stops == 0 and i.distance < num:
            num_of_routes += 1
            continue
        if i.stops == 0 and i.distance > num:
            continue

        if i.distance / i.stops < num:
            num_of_routes += 1
    return num_of_routes


def func2(listt, City):
    list_res = []
    for i in listt:
        if i.a == City:
            list_res.append(i)
    return list_res




with open("routes", "r") as f:
    list_of_tuple_routes = []
    for route in f:
        a, b, d, c = route.split()
        data_tuple = (a, b, d, c)
        list_of_tuple_routes.append(data_tuple)


List_of_objects_routes = [Route(*x) for x in list_of_tuple_routes]

max_stops_obj = max(List_of_objects_routes, key=lambda x: x.stops)

for i in List_of_objects_routes:
    if i.stops == max_stops_obj.stops:
        print(i)






