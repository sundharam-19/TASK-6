class Vehicle:
    """
    Base class for all vehicles in the rental system.
    """
    def __init__(self, model, rental_rate_per_day):
        self.model = model
        self.rental_rate_per_day = rental_rate_per_day

    def calculate_rental(self, duration_days):
        """
        Calculates the total rental cost based on duration.
        This is a generic calculation; subclasses can override it.
        """
        if duration_days <= 0:
            return 0
        return self.rental_rate_per_day * duration_days

    def __str__(self):
        return f"{self.__class__.__name__} Model: {self.model}"

class Car(Vehicle):
    """
    Car subclass with a potential discount for longer rentals (e.g., > 3 days).
    """
    def __init__(self, model, rental_rate_per_day, seats):
        super().__init__(model, rental_rate_per_day)
        self.seats = seats

    def calculate_rental(self, duration_days):
        """
        Applies a 10% discount if rented for more than 3 days.
        """
        base_cost = super().calculate_rental(duration_days)
        if duration_days > 3:
            return base_cost * 0.9 # 10% discount
        return base_cost

class Bike(Vehicle):
    """
    Bike subclass with a flat processing fee per rental.
    """
    def __init__(self, model, rental_rate_per_day, engine_cc):
        super().__init__(model, rental_rate_per_day)
        self.engine_cc = engine_cc
        self.processing_fee = 50 # Flat fee

    def calculate_rental(self, duration_days):
        """
        Adds a flat processing fee to the total cost.
        """
        base_cost = super().calculate_rental(duration_days)
        return base_cost + self.processing_fee

class Truck(Vehicle):
    """
    Truck subclass with a cost calculation based on cargo capacity weight.
    """
    def __init__(self, model, rental_rate_per_day, capacity_tonnes):
        super().__init__(model, rental_rate_per_day)
        self.capacity_tonnes = capacity_tonnes
        self.heavy_duty_surcharge_per_tonne = 20

    def calculate_rental(self, duration_days):
        """
        Adds a surcharge based on the truck's capacity to the total cost.
        """
        base_cost = super().calculate_rental(duration_days)
        surcharge = self.capacity_tonnes * self.heavy_duty_surcharge_per_tonne * duration_days
        return base_cost + surcharge

# --- Demonstration of Polymorphism ---

# Create instances of different vehicles
vehicle1 = Car("Toyota Camry", 60, seats=5)
vehicle2 = Bike("Harley Davidson", 30, engine_cc=1800)
vehicle3 = Truck("Ford F-150", 100, capacity_tonnes=2.5)

# Define rental duration
rental_duration = 5 # days

# Use a list to process vehicles polymorphically
vehicles_to_rent = [vehicle1, vehicle2, vehicle3]

print(f"Calculating rental costs for {rental_duration} days:")

for vehicle in vehicles_to_rent:
    # The same method call works for all objects, but the specific
    # implementation (polymorphism) depends on the object's actual class.
    cost = vehicle.calculate_rental(rental_duration)
    print(f"- {vehicle}: Total Cost = ${cost:.2f}")