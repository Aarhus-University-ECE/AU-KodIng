def serve_next_customer():
    pass

customers_in_queue = ["Kim Possible","Peppa Pig","Ferb","Phineas"]
while len(customers_in_queue) > 0:
    serve_next_customer()
    customers_in_queue = customers_in_queue[1:] 
    print(customers_in_queue)