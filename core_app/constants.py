BUY = "buy"
SALE = "sale"
RENT = "rent"
PROPERTY_FOR_TYPES = (
    (BUY, "Buy"),
    (SALE, "Sale"),
    (RENT, "Rent")
)
HOLD = "hold"
OPEN = "open"
CLOSED = "closed"
PROPERTY_STATUS = (
    (HOLD, "Hold"),
    (OPEN, "Open"),
    (CLOSED, "Closed")
)
NEW = "new"
RESALE = "resale"
PROPERTY_TYPE = (
    (NEW, "New"),
    (RESALE, "Resale")
)
FURNISHED = "furnished"
SEMIFURNISHED = "semifurnished"
UNFURNISHED = "unfurnished"
FURNITURE_TYPE = (
    (FURNISHED, "Furnished"),
    (SEMIFURNISHED, "Semi-furnished"),
    (UNFURNISHED, "Unfurnished")
)
EAST = "east"
WEST = "west"
SOUTH = "south"
NORTH = "north"
NORTH_EAST = "north-east"
NORTH_WEST = "north-west"
SOUTH_EAST = "south-east"
SOUTH_WEST = "south-west"
PROPERTY_FACING = (
    (EAST, "east"),
    (WEST, "west"),
    (SOUTH, "south"),
    (NORTH, "north"),
    (NORTH_EAST, "north-east"),
    (NORTH_WEST, "north-west"),
    (SOUTH_EAST, "south-east"),
    (SOUTH_WEST, "south-west")
)

FREEHOLD = "freehold"
LEASEHOLD = "leasehold"
POWER_OF_ATTORNEY = "power of attorney"
COOPERATIVE_SOCIETY = "cooperative society"
TYPE_OF_OWNERSHIP = (
    (FREEHOLD, "Freehold"),
    (LEASEHOLD, "Leasehold"),
    (POWER_OF_ATTORNEY, "Power of attorney"),
    (COOPERATIVE_SOCIETY, "Cooperative society"),
)
BACHELOR = "bachelor"
FAMILY = "family"
ALLOWED_FOR = (
    (NEW, "Bachelor"),
    (FAMILY, "Family")
)