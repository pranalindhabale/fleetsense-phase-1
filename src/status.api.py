# Status Change API - Ticket Management System
# Role comes from logged-in user, NEVER from request body

ALLOWED_TRANSITIONS = {
    "Open": ["In Progress"],
    "In Progress": ["Resolved"],
    "Resolved": ["Closed"],
    "Closed": [],
}

tickets = [
    {"id": 1, "title": "Login not working", "status": "Open"},
    {"id": 2, "title": "Payment failed", "status": "In Progress"},
    {"id": 3, "title": "Report not loading", "status": "Resolved"},
]

def change_status(ticket_id, new_status, logged_in_user):
    if logged_in_user.get("role") not in ["agent", "admin"]:
        return {"error": "Permission denied: only agent/admin can change status"}
    ticket = next((t for t in tickets if t["id"] == ticket_id), None)
    if not ticket:
        return {"error": "Ticket not found"}
    current = ticket["status"]
    if new_status not in ALLOWED_TRANSITIONS.get(current, []):
        return {"error": f"Cannot change from {current} to {new_status}"}
    ticket["status"] = new_status
    return {"success": True, "ticket": ticket}

if __name__ == "__main__":
    user = {"name": "pranali", "role": "agent"}
    print(change_status(1, "In Progress", user))
    print(change_status(1, "Closed", user))
    print(change_status(3, "Closed", user))
