class Box:
    def __init__(self, dimensions, box_id):
        self.dimensions = dimensions
        self.id = box_id
    
    def fits_inside(self, other_box):
        self_dimensions_sorted = sorted(self.dimensions, reverse=True)
        other_dimensions_sorted = sorted(other_box.dimensions, reverse=True)
        
        return all(self_dimensions_sorted[i] < other_dimensions_sorted[i] for i in range(3))
    
    def __repr__(self):
        return f"Box({self.id}, {self.dimensions})"
    
    def __lt__(self, other):
        # Define a comparação para '<' (menor que)
        return self.dimensions < other.dimensions
    
    def __eq__(self, other):
        # Define a comparação para '==' (igual a)
        return self.dimensions == other.dimensions
