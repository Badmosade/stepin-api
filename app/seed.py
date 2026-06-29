from app.core.database import SessionLocal
from app.models.category import Category
from app.models.state import State
from app.models.resource import Resource


def seed_categories():
    db = SessionLocal()
    categories = [
        {"name": "Legal Aid", "description": "Legal assistance and immigration lawyers"},
        {"name": "Housing", "description": "Housing assistance and shelter programs"},
        {"name": "Healthcare", "description": "Free and low cost medical services"},
        {"name": "Food Assistance", "description": "Food banks and nutrition programs"},
        {"name": "Employment", "description": "Job placement and career services"},
        {"name": "Education", "description": "ESL classes and GED programs"},
        {"name": "Certifications", "description": "Quick certifications for employment"},
        {"name": "Language Support",
            "description": "Translation and interpretation services"},
    ]
    for c in categories:
        exists = db.query(Category).filter(Category.name == c["name"]).first()
        if not exists:
            db.add(Category(**c))
    db.commit()
    db.close()
    print("Categories seeded.")


def seed_states():
    db = SessionLocal()
    states = [
        {"name": "California", "abbreviation": "CA"},
        {"name": "Texas", "abbreviation": "TX"},
        {"name": "New York", "abbreviation": "NY"},
        {"name": "Florida", "abbreviation": "FL"},
        {"name": "Illinois", "abbreviation": "IL"},
        {"name": "Georgia", "abbreviation": "GA"},
        {"name": "Arizona", "abbreviation": "AZ"},
        {"name": "Washington", "abbreviation": "WA"},
        {"name": "Virginia", "abbreviation": "VA"},
        {"name": "New Jersey", "abbreviation": "NJ"},
    ]
    for s in states:
        exists = db.query(State).filter(State.name == s["name"]).first()
        if not exists:
            db.add(State(**s))
    db.commit()
    db.close()
    print("States seeded.")


def seed_resources():
    db = SessionLocal()
    resources = [
        {
            "name": "ACLU of California",
            "description": "Free legal aid for immigrants facing deportation and discrimination",
            "address": "39 Drumm Street, San Francisco, CA 94111",
            "phone": "415-621-2493",
            "website": "https://www.acluca.org",
            "state_id": 1,
            "category_id": 1
        },
        {
            "name": "LA Family Housing",
            "description": "Housing assistance and shelter for immigrants in Los Angeles",
            "address": "7843 Lankershim Blvd, North Hollywood, CA 91605",
            "phone": "818-982-9648",
            "website": "https://www.lafh.org",
            "state_id": 1,
            "category_id": 3
        },
        {
            "name": "Texas RioGrande Legal Aid",
            "description": "Free civil legal services for low income immigrants in Texas",
            "address": "4920 N IH-35, Austin, TX 78751",
            "phone": "512-374-2700",
            "website": "https://www.trla.org",
            "state_id": 2,
            "category_id": 1
        },
        {
            "name": "New York Immigration Coalition",
            "description": "Advocacy and resources for immigrants across New York",
            "address": "131 West 33rd Street, New York, NY 10001",
            "phone": "212-627-2227",
            "website": "https://www.nyic.org",
            "state_id": 3,
            "category_id": 1
        },
        {
            "name": "Federally Qualified Health Centers Florida",
            "description": "Low cost healthcare for uninsured immigrants in Florida",
            "address": "Various locations across Florida",
            "phone": "1-800-984-3272",
            "website": "https://www.flhealthcharts.gov",
            "state_id": 4,
            "category_id": 4
        },
    ]
    for r in resources:
        exists = db.query(Resource).filter(Resource.name == r["name"]).first()
        if not exists:
            db.add(Resource(**r))
    db.commit()
    db.close()
    print("Resources seeded.")


if __name__ == "__main__":
    seed_categories()
    seed_states()
    seed_resources()
