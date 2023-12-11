def create_class_point(name, base, attrs):
    attrs.update({'Max_ccord' : 100, 'Min_coord' : 0})
    return type(name, base, attrs)

class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)