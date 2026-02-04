import json
import math
import random
from datetime import datetime, timezone
from typing import Dict, List, Tuple

COUNTRIES: List[Dict[str, object]] = [
    {
        "id": "japan",
        "country": "Japan",
        "capital": "Tokyo",
        "lat": 35.6762,
        "lng": 139.6503,
        "region": "East Asia",
        "hemisphere_lat": "Northern",
        "hemisphere_lng": "Eastern",
        "neighbors": ["Russia", "China", "South Korea"],
        "terrain": "volcanic mountains and pacific coast plains",
        "claim": "a neon-lit megacity balancing anime dens with imperial gardens",
        "fun_fact": "Shinjuku Station in Tokyo moves more passengers daily than any other transport hub on Earth.",
        "zoom": 3.5
    },
    {
        "id": "brazil",
        "country": "Brazil",
        "capital": "Brasilia",
        "lat": -15.7939,
        "lng": -47.8828,
        "region": "Central Brazil",
        "hemisphere_lat": "Southern",
        "hemisphere_lng": "Western",
        "neighbors": ["Bolivia", "Peru", "Argentina"],
        "terrain": "cerrado savannahs and futuristic axial avenues",
        "claim": "a planned city shaped like an airplane when viewed from above",
        "fun_fact": "Brasilia's pilots--the residential wings--were designed in just 41 months by Oscar Niemeyer.",
        "zoom": 4.2
    },
    {
        "id": "kenya",
        "country": "Kenya",
        "capital": "Nairobi",
        "lat": -1.2864,
        "lng": 36.8172,
        "region": "East Africa",
        "hemisphere_lat": "Southern",
        "hemisphere_lng": "Eastern",
        "neighbors": ["Tanzania", "Ethiopia", "Somalia"],
        "terrain": "Great Rift Valley escarpments and savannah grasslands",
        "claim": "safaris launching just minutes from the CBD",
        "fun_fact": "Nairobi is the only capital city with a fully-fledged national park at its edge.",
        "zoom": 5.1
    },
    {
        "id": "canada",
        "country": "Canada",
        "capital": "Ottawa",
        "lat": 45.4215,
        "lng": -75.6972,
        "region": "Ontario-Quebec corridor",
        "hemisphere_lat": "Northern",
        "hemisphere_lng": "Western",
        "neighbors": ["United States"],
        "terrain": "maple-lined boulevards and parliament perched by a river gorge",
        "claim": "ice skating on a UNESCO World Heritage canal every winter",
        "fun_fact": "Ottawa's Rideau Canal becomes the world's largest naturally frozen skating rink.",
        "zoom": 4.8
    },
    {
        "id": "australia",
        "country": "Australia",
        "capital": "Canberra",
        "lat": -35.2809,
        "lng": 149.13,
        "region": "Australian Capital Territory",
        "hemisphere_lat": "Southern",
        "hemisphere_lng": "Eastern",
        "neighbors": ["New South Wales"],
        "terrain": "bush hills, eucalyptus groves, and a sculpted man-made lake",
        "claim": "radial avenues inspired by the geometry of Washington D.C. and Paris",
        "fun_fact": "Canberra was selected as a compromise between rivals Sydney and Melbourne in 1908.",
        "zoom": 5.2
    },
    {
        "id": "spain",
        "country": "Spain",
        "capital": "Madrid",
        "lat": 40.4168,
        "lng": -3.7038,
        "region": "Iberian plateau",
        "hemisphere_lat": "Northern",
        "hemisphere_lng": "Western",
        "neighbors": ["Portugal", "France"],
        "terrain": "high plateau meseta with grand boulevards and royal plazas",
        "claim": "late-night plazas buzzing with tapas and flamenco energy",
        "fun_fact": "Madrid sits 667 meters above sea level, making it one of Europe's highest capitals.",
        "zoom": 5.4
    },
    {
        "id": "egypt",
        "country": "Egypt",
        "capital": "Cairo",
        "lat": 30.0444,
        "lng": 31.2357,
        "region": "Lower Nile Valley",
        "hemisphere_lat": "Northern",
        "hemisphere_lng": "Eastern",
        "neighbors": ["Sudan", "Libya"],
        "terrain": "delta oasis textures meeting desert plateaus",
        "claim": "minarets and Nile bridges framed by ancient pyramids",
        "fun_fact": "Greater Cairo is nicknamed the City of a Thousand Minarets thanks to its skyline.",
        "zoom": 5.0
    },
    {
        "id": "india",
        "country": "India",
        "capital": "New Delhi",
        "lat": 28.6139,
        "lng": 77.209,
        "region": "Indo-Gangetic plains",
        "hemisphere_lat": "Northern",
        "hemisphere_lng": "Eastern",
        "neighbors": ["Pakistan", "Nepal", "Bangladesh"],
        "terrain": "ceremonial axes, Mughal gardens, and bustling bazaars",
        "claim": "where Rajpath stretches from the presidential palace to India Gate",
        "fun_fact": "New Delhi's Connaught Place is among the world's most expensive office markets.",
        "zoom": 4.8
    },
    {
        "id": "chile",
        "country": "Chile",
        "capital": "Santiago",
        "lat": -33.4489,
        "lng": -70.6693,
        "region": "Central Valley of Chile",
        "hemisphere_lat": "Southern",
        "hemisphere_lng": "Western",
        "neighbors": ["Argentina", "Bolivia", "Peru"],
        "terrain": "Andean peaks wrapping a Mediterranean basin",
        "claim": "vineyards and ski slopes visible in the same skyline",
        "fun_fact": "Santiago is ringed by the Andes, giving sunsets an intense copper glow after rain.",
        "zoom": 5.2
    },
    {
        "id": "iceland",
        "country": "Iceland",
        "capital": "Reykjavik",
        "lat": 64.1466,
        "lng": -21.9426,
        "region": "Atlantic Nordic",
        "hemisphere_lat": "Northern",
        "hemisphere_lng": "Western",
        "neighbors": ["Greenland"],
        "terrain": "geothermal pools, corrugated lava fields, and midnight sun festivals",
        "claim": "the world's northernmost sovereign capital",
        "fun_fact": "Reykjavik heats almost every home with geothermal energy tapped from volcanic soil.",
        "zoom": 4.6
    },
    {
        "id": "indonesia",
        "country": "Indonesia",
        "capital": "Jakarta",
        "lat": -6.2088,
        "lng": 106.8456,
        "region": "Java Island",
        "hemisphere_lat": "Southern",
        "hemisphere_lng": "Eastern",
        "neighbors": ["Malaysia", "Singapore", "Australia"],
        "terrain": "monsoon-soaked skyscrapers built on a sprawling delta",
        "claim": "the tropical megacity where 13 rivers meet the Java Sea",
        "fun_fact": "Jakarta's Old Town still shows Dutch colonial canals dating back 400 years.",
        "zoom": 4.5
    },
    {
        "id": "morocco",
        "country": "Morocco",
        "capital": "Rabat",
        "lat": 34.0209,
        "lng": -6.8416,
        "region": "Atlantic Maghreb",
        "hemisphere_lat": "Northern",
        "hemisphere_lng": "Western",
        "neighbors": ["Algeria", "Western Sahara"],
        "terrain": "Atlantic cliffs meeting Andalusian-inspired medinas",
        "claim": "oceanfront kasbah walls painted in cobalt blues",
        "fun_fact": "Rabat hosts Mawazine, one of the largest music festivals on the African continent.",
        "zoom": 5.2
    }
]

WORLD_FACTS_BASE = [
    "The prime meridian slices directly through Greenwich, London, dividing east from west longitudes.",
    "Mount Chimborazo in Ecuador is the farthest point from Earth's core thanks to equatorial bulge.",
    "Africa is the only continent to stretch from the northern temperate zone into the southern temperate zone.",
    "Canada has more lakes than the rest of the world combined, holding nearly 20% of global fresh surface water.",
    "Antarctica holds about 90% of the world's fresh ice, yet it is considered a desert because of minimal precipitation.",
    "Australia is wider than the moon--the continent measures roughly 4,000 km coast-to-coast.",
    "Spain's Puerta del Sol square is the literal kilometer zero for the nation's radial road network.",
    "Jakarta is subsiding so rapidly that Indonesia is building a new capital--Nusantara--on the island of Borneo.",
    "Morocco's Atlas Mountains create rain shadows that feed the Sahara's dune systems.",
    "Chile stretches over 4,200 km north-south while averaging only 180 km east-west."
]

INSPIRATIONS = [
    "Sketch a map tracing the hemispheres mentioned in the clues.",
    "Chart the travel time between these capitals using great-circle routes.",
    "Design a mini field journal page capturing the terrain keywords from the hints.",
    "Create a choropleth showing which neighbors share borders with the spotlight country.",
    "Use string art to connect all hinted coordinates on a blank world outline.",
    "Imagine a rail line linking the featured capitals and storyboard the journey stops.",
    "Layer satellite imagery to compare the terrain descriptors with actual topography."
]


def _hemisphere_label(value: float, *, latitude: bool = True) -> str:
    if latitude:
        return "North" if value >= 0 else "South"
    return "East" if value >= 0 else "West"


def _format_degrees(value: float, *, latitude: bool) -> str:
    hemi = _hemisphere_label(value, latitude=latitude)
    return f"{abs(value):.1f} deg {hemi}"


def _random_country() -> Dict[str, object]:
    return random.choice(COUNTRIES)


def _haversine_km(origin: Tuple[float, float], destination: Tuple[float, float]) -> float:
    radius = 6371.0
    lat1, lon1 = map(math.radians, origin)
    lat2, lon2 = map(math.radians, destination)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c


def _capital_challenge() -> Dict[str, object]:
    entry = _random_country()
    hints = [
        f"Plot {entry['country']} in the {entry['region']} region.",
        f"Latitude sits near {_format_degrees(entry['lat'], latitude=True)}.",
        f"Longitude drifts around {_format_degrees(entry['lng'], latitude=False)}.",
        f"Expect {entry['terrain']}.",
        f"{entry['country']} rubs shoulders with {', '.join(entry['neighbors'])}."
        if entry["neighbors"]
        else f"{entry['country']} is uniquely positioned with few direct land neighbors.",
        f"Locals brag about {entry['claim']}."
    ]
    random.shuffle(hints)
    return {
        "id": f"capital-{entry['id']}",
        "title": "Capital Quest",
        "type": "Capital Quest",
        "prompt": f"Which capital city anchors {entry['country']}?",
        "answer": entry["capital"],
        "hints": hints[:3],
        "fun_fact": entry["fun_fact"],
        "location": {"lat": entry["lat"], "lng": entry["lng"], "zoom": entry["zoom"]},
    }


def _country_locator_challenge() -> Dict[str, object]:
    entry = _random_country()
    neighbor_hint = (
        f"It touches {random.choice(entry['neighbors'])} along a storied frontier."
        if entry["neighbors"]
        else "It stands apart from most continental borders."
    )
    hints = [
        neighbor_hint,
        f"You will cross {_format_degrees(entry['lat'], latitude=True)} when visiting.",
        f"The capital is famed for {entry['claim']}.",
        f"Cartographers log it within the {entry['region']} macro-region.",
        f"Expect landscapes of {entry['terrain']}."
    ]
    random.shuffle(hints)
    return {
        "id": f"country-{entry['id']}",
        "title": "Country Sleuth",
        "type": "Country Sleuth",
        "prompt": f"A field notebook lists coordinates {_format_degrees(entry['lat'], latitude=True)} and {_format_degrees(entry['lng'], latitude=False)}. Which country were they surveying?",
        "answer": entry["country"],
        "hints": hints[:3],
        "fun_fact": entry["fun_fact"],
        "location": {"lat": entry["lat"], "lng": entry["lng"], "zoom": entry["zoom"]},
    }


def _distance_flash_challenge() -> Dict[str, object]:
    origin, destination = random.sample(COUNTRIES, 2)
    distance = _haversine_km(
        (origin["lat"], origin["lng"]),
        (destination["lat"], destination["lng"])
    )
    hints = [
        f"Leg one launches from {origin['capital']}, known for {origin['claim']}.",
        f"Leg two lands in {destination['capital']}, amidst {destination['terrain']}.",
        f"Both cities sit in the {origin['hemisphere_lat']} Hemisphere and {destination['hemisphere_lat']} Hemisphere respectively.",
        f"Prepare to traverse roughly {distance:,.0f} km over the curve of Earth."
    ]
    random.shuffle(hints)
    midpoint_lat = (origin["lat"] + destination["lat"]) / 2
    midpoint_lng = (origin["lng"] + destination["lng"]) / 2
    return {
        "id": f"distance-{origin['id']}-{destination['id']}",
        "title": "Great Circle Dash",
        "type": "Great Circle Dash",
        "prompt": f"Name the two capital cities connected by this great-circle hop of about {distance:,.0f} km.",
        "answer": f"{origin['capital']} <-> {destination['capital']}",
        "hints": hints[:3],
        "fun_fact": f"The route links {origin['country']} and {destination['country']}, crossing {abs(midpoint_lat):.1f} deg latitude midway.",
        "location": {
            "lat": midpoint_lat,
            "lng": midpoint_lng,
            "zoom": min(max(3.2, 7 - distance / 4000), 5.5)
        },
    }


def _random_world_fact() -> str:
    fact = random.choice(WORLD_FACTS_BASE)
    if random.random() < 0.55:
        anchors = random.sample(COUNTRIES, 2)
        distance = _haversine_km(
            (anchors[0]["lat"], anchors[0]["lng"]),
            (anchors[1]["lat"], anchors[1]["lng"])
        )
        fact = (
            f"If you trek from {anchors[0]['capital']} to {anchors[1]['capital']}, "
            f"you'll trace roughly {distance:,.0f} km along Earth's curvature."
        )
    return fact


def _random_inspiration() -> str:
    return random.choice(INSPIRATIONS)


CHALLENGE_BUILDERS = [
    _capital_challenge,
    _country_locator_challenge,
    _distance_flash_challenge,
]


def handler(_request):
    challenge = random.choice(CHALLENGE_BUILDERS)()
    payload = {
        "challenge": challenge,
        "world_fact": _random_world_fact(),
        "inspiration": _random_inspiration(),
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(payload),
    }
