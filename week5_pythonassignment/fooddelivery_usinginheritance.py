class DeliveryPartner:
    def __init__(self, name, partner_id, deliveries):
        self.name = name
        self.partner_id = partner_id
        self.deliveries = deliveries

    def total_earning(self):
        return 0

    def display(self):
        print(f'{self.name} ({self.partner_id}) -- Deliveries: {self.deliveries} -- Earned: NPR {self.total_earning()}')


class BikeRider(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, km_travelled):
        super().__init__(name, partner_id, deliveries)
        self.km_travelled = km_travelled

    def total_earning(self):
        return (self.deliveries * 80) + (self.km_travelled * 5)


class Walker(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, rainy_deliveries):
        super().__init__(name, partner_id, deliveries)
        self.rainy_deliveries = rainy_deliveries

    def total_earning(self):
        return (self.deliveries * 60) + (self.rainy_deliveries * 50)


class CarDriver(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, fuel_cost):
        super().__init__(name, partner_id, deliveries)
        self.fuel_cost = fuel_cost

    def total_earning(self):
        return (self.deliveries * 120) - self.fuel_cost


partners = [
    BikeRider('Nitesh Shahi', 'Ba01', 10, 100),
    Walker('Gopal Sharma', 'Ga01', 12, 5),
    CarDriver('Ashim Acharya', 'Na01', 8, 500),
]

for p in partners:
    p.display()

top = max(partners, key=lambda p: p.total_earning())
print(f'Highest Earner: {top.name} - NPR {top.total_earning()}')