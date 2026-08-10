raw_tickets = [ 
    {"ticket_id": "TCK001", "movie": "Avengers: Endgame", "price": 120000, "seat": "A12", "status": 
    "booked"}, 
    {"ticket_id": " tck002 ", "movie": "Spider-man: No Way Home", "price": 150000, "seat": "B05", "status": 
    "available"}, 
    {"ticket_id": "TCK003", "movie": "The Batman", "price": 130000, "seat": "C08", "status": "booked"}, 
    {"ticket_id": "TCK004", "movie": "Superman: Legacy", "price": 140000, "seat": "D10", "status": 
    "cancelled"}, 
    {"ticket_id": "TCK005", "movie": "Ironman: Rise of Technovore", "price": 160000, "seat": "E15", "status": 
    "booked"} 
    
] 

#cau 1 
def clean_and_validate_tickets():
    for ticket in raw_tickets:
        ticket["ticket_id"] = ticket["ticket_id"].strip().upper()
        validate = ticket["ticket_id"][3:]
        if ticket["ticket_id"].startswith("TCK") and validate.isdigit() and len(validate) >= 3:
            continue
        else:
            raw_tickets.remove(ticket)

clean_and_validate_tickets()
print(raw_tickets)

def search_tickets():
    price = input("Nhập giá trị cần tìm: ")
    status = input("Nhập trạng thái vé: ")
    search = []
    for ticket in raw_tickets:
        if ticket["price"] <= int(price) or ticket["status"] == status:
            search.append(ticket)

    print("Các vé tìm thấy: ",search)

search_tickets()

def sort_tickets_by_price_asc():
    n = len(raw_tickets)
    for i in range(n):
        for j in range(n-i-1):
            if raw_tickets[j]["price"] > raw_tickets[j + 1]["price"]:
                raw_tickets[i],raw_tickets[j+1] = raw_tickets[j+1], raw_tickets[j]

    print(raw_tickets)

sort_tickets_by_price_asc()